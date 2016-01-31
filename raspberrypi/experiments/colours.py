"""colours.py - Control a LEDs using a Raspberry Pi. 

At the console, use the following keys to control the five LEDs. 

Press 'Ctrl+c' or 'x' to exit.
Press 'r', 'y', 'g', 'w', 'b' to toggle red, yellow, green, white, and blue, respectively.
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

control_pins = [14, 15, 18, 23, 24]
state = [0, 0, 0, 0, 0]

GPIO.setmode(GPIO.BCM)
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

actions = {'r':0,
           'y':1,
           'g':2,
           'w':3,
           'b':4,
          }

try:
  while True:
    character = getch()
    if character == 'x' or character == '0x03':
      GPIO.cleanup()
      exit()
    elif character in actions:
      print ('> ' + character)
      state[actions[character]] = 1 - state[actions[character]]
      GPIO.output(control_pins[actions[character]], state[actions[character]]) 

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
