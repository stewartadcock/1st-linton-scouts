"""motors-dc-pwm.py - Control a pair of DC motors using a Raspberry Pi with pulse width modulation to control speed. 

This drives the dual L9110 H-bridge driver GPIO circuit with two DC motors. See l9110.md for details. 
At the console, use the following keys to control the two motors. 

Press 'Ctrl+c' or 'x' to exit.
Press 'a', 'z', 'n', 'm' for forward, backward, right-only, left-only.
Press 'j', 'k' for rotate left, right.
Press 'f', 'v' for faster, slower.
Press ' ' to stop.
"""

import RPi.GPIO as GPIO
import sys
import termios
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
p = []

GPIO.setmode(GPIO.BCM)
for pin in range(0, len(control_pins)):
  GPIO.setup(control_pins[pin], GPIO.OUT)
  GPIO.output(control_pins[pin], False)
  p.append(GPIO.PWM(control_pins[pin], 40))

actions = {'a':[1,0,1,0],
           'z':[0,1,0,1],
           'n':[1,0,0,0],
           'm':[0,0,1,0],
           'j':[0,1,1,0],
           'k':[1,0,0,1],
           ' ':[0,0,0,0],
          }

speed = 50

try:
  while True:
    character = getch()
    if character == 'x' or character == '0x03':
      GPIO.cleanup()
      exit()
    elif character == 'f' and speed < 100:
      speed = speed + 10
      print ('speed = {0}%'.format(speed))
      for pin in range(0, len(control_pins)):
        p[pin].ChangeDutyCycle(speed) 
    elif character == 'v' and speed > 0:
      speed = speed - 10
      print ('speed = {0}%'.format(speed))
      for pin in range(0, len(control_pins)):
        p[pin].ChangeDutyCycle(speed) 
    elif character in actions:
      print ('> ' + character)
      for pin in range(0, len(control_pins)):
        if actions[character][pin] != 0: 
          p[pin].start(speed) 
        else:
          p[pin].stop() 

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
