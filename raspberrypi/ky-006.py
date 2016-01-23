"""ky-006.py - demo script for KY-006 GPIO circuit - a passive buzzer.                                                                                          

See ky-006.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
  while True:
    for i in range(1,int(0.2/0.0002)):
      GPIO.output(24, True)
      time.sleep(0.0002)
      GPIO.output(24, False)
      time.sleep(0.0002)

    for i in range(1,int(0.2/0.01)):
      GPIO.output(24, True)
      time.sleep(0.01)
      GPIO.output(24, False)
      time.sleep(0.01)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
