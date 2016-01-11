"""ky-012.py - demo script for KY-012 GPIO circuit - an active buzzer.
See ky-012.md for details. 
Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
  while True:
    GPIO.output(24, True)
    time.sleep(0.2)
    GPIO.output(24, False)
    time.sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
