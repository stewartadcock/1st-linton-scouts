"""led.py - demo script for LED GPIO circuit.

See led.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

sleep_time = 0.6

try:
  while True:
    GPIO.output(12, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.output(12, GPIO.LOW)
    time.sleep(sleep_time)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
