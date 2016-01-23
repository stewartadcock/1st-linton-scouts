"""hc-sr501.py - demo script for HC-SR501 GPIO circuit - an IR motion sensor.

See hc-sr501.md for details. 

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

signal_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(signal_pin, GPIO.IN)

try:
  while True:
    time.sleep(0.1)

    while GPIO.input(signal_pin)==0:
      pass

    print ("Motion detected!")

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
