"""pi-sheep.py - Control the Raspberry Pi-powered Pi-Sheep. 

This drives the dual L9110 H-bridge driver GPIO circuit with two DC motors. See l9110.md for details. 
At the console, use the following keys to control the two motors. The version has an Ovine twist.

This script requires Python3.

Press 'Ctrl+c' or 'x' to exit.

Press 'a', 'z', 'n', 'm' for forward, backward, right-only, left-only.
Press 'j', 'k' rotate left, right.
Press ' ' to stop the motors.

Press 'r', 'e', 's' to record instructions, play instructions, stop recording instructions.
"""

import RPi.GPIO as GPIO
import sys
import termios
import time
import tty

# As we know that this is a POSIX system, we can define a getch-like function that manipulates the tty.
def getch():
  """Return a single character from stdin.
  """
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(fd)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch

print (__doc__)

control_pins = [24, 23, 25, 18]

GPIO.setmode(GPIO.BCM)
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

actions = {'a':[1,0,1,0],
           'z':[0,1,0,1],
           'n':[1,0,0,0],
           'm':[0,0,1,0],
           'j':[0,1,1,0],
           'k':[1,0,0,1],
           ' ':[0,0,0,0],
          }

playbook = []
record_start = None

try:
  while True:
    character = getch()
    if character == 'x' or character == '0x03':
      print ()
      GPIO.cleanup()
      exit()
    elif character == 'r':
      record_start = time.time()
      playbook = []
    elif character == 's':
      record_start = None
    elif character == 'e':
      record_start = None
      playback_start = time.time()
      for (t, a) in playbook:
        while time.time() < t + playback_start: # should sleep instead!
          pass
        print (a, end="", flush=True)
        for pin in range(0, len(control_pins)):
          GPIO.output(control_pins[pin], actions[a][pin] != 0) 
    elif character in actions:
      print (character, end="", flush=True)
      if record_start:
        t = time.time() - record_start
        playbook.append((t, character))
      for pin in range(0, len(control_pins)):
        GPIO.output(control_pins[pin], actions[character][pin] != 0) 

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
