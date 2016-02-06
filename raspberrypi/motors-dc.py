"""motors-dc.py - Control a pair of DC motors using a Raspberry Pi. 

This drives the dual L9110 H-bridge driver GPIO circuit with two DC motors. See l9110.md for details. 
At the console, use the following keys to control the two motors. 

Press 'Ctrl+c' or 'x' to exit.
Press 'a', 'z', 'n', 'm' for forward, backward, right-only, left-only.
Press ' ' to stop.
What do you think 'j' and 'k' will do?

As an exercise, can you adjust this script to control the motor speed too?
Tip: what happens if you start and stop the motors rapidly?
"""

import RPi.GPIO as GPIO
import sys
import termios
import time
import tty

# As we know that this is a POSIX system, we can define a getch-like function that manipulates the tty.
def getch():
  """Return a singke character from stdin.
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

try:
  while True:
    character = getch()
    if character == 'x' or character == '0x03':
      GPIO.cleanup()
      exit()
    elif character in actions:
      print ('> ' + character)
      for pin in range(0, len(control_pins)):
        GPIO.output(control_pins[pin], actions[character][pin] != 0) 
    else:
      for pin in control_pins:
        GPIO.output(pin, False)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
