"""led-array.py - demo script for LED array GPIO circuit.

See led-array.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

import RPi.GPIO as GPIO
import time

array_pins = [10, 9, 11, 0, 5]
sequence = [10, 9, 11, 0, 5, 0, 11, 9]

GPIO.setmode(GPIO.BCM)
for pin in array_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)

sleep_time = 0.2

try:
  while True:
    for pin in sequence:
      GPIO.output(pin, GPIO.HIGH)
      time.sleep(sleep_time)
      GPIO.output(pin, GPIO.LOW)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
