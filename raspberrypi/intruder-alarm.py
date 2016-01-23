"""intruder-alarm.py - a GPIO IR motion sensing alarm.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

signal_pin = 16
buzz_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal_pin, GPIO.IN)
GPIO.setup(buzz_pin, GPIO.OUT)

try:
  while True:
    time.sleep(0.1)

    while not GPIO.input(signal_pin):
      pass

    GPIO.output(buzz_pin, True)
    time.sleep(1)
    GPIO.output(buzz_pin, False)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
