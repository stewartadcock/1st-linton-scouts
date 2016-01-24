"""ky-012.py - demo script for KY-012 GPIO circuit - an active buzzer.
See ky-012.md for details. 
Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

buzz_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_pin, GPIO.OUT)

try:
  while True:
    GPIO.output(buzz_pin, True)
    time.sleep(0.2)
    GPIO.output(buzz_pin, False)
    time.sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
