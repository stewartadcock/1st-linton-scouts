"""led-array.py - demo script for LED array GPIO circuit.

See led.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

import RPi.GPIO as GPIO
import time

array_pins = [10, 9, 11, 0, 5]

red = 11
yellow = 0
green = 5

GPIO.setmode(GPIO.BCM)
for pin in array_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

time_ryg = [(2.0, 0, 0, 1),
            (0.5, 0, 1, 0),
            (2.0, 1, 0, 0),
            (1.0, 1, 1, 0)]

try:
  while True:
    for s in time_ryg:
      GPIO.output(red, s[1])
      GPIO.output(yellow, s[2])
      GPIO.output(green, s[3])
      time.sleep(s[0])

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
