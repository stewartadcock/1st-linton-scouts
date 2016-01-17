"""l9110-dual-dc.py - demo script for dual L9110 GPIO circuit with a pair of 5v0 dc motors.

See l9110-dual-dc.md for details. 

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

step_time = 1.5

try:
  while True:
    GPIO.output(23, True)
    GPIO.output(17, True)
    print('1-0 1-0')
    time.sleep(step_time)

    GPIO.output(23, False)
    print('0-0 1-0')
    time.sleep(step_time)

    GPIO.output(25, True)
    GPIO.output(22, True)
    GPIO.output(17, False)
    print('0-1 0-1')
    time.sleep(step_time)

    GPIO.output(25, False)
    GPIO.output(22, False)
    print('0-0 0-0')
    time.sleep(step_time)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
