"""tcrt5000.py - demo script for TCRT5000 GPIO circuit - an IR Proximity Sensor.

See tcrt5000.md for details. 

'.' is output if reflection is detected; 'X', otherwise.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN)

try:
  while True:
    time.sleep(0.1)

    if GPIO.input(22):
      print ('.')
    else:
      print ('X')

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
