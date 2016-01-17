"""hc-sr04.py - demo script for HC-SR04 GPIO circuit - an ultrasonic distance ranger.

See hc-sr04.md for details. 

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) # Signal
GPIO.setup(22, GPIO.IN) # Echo

GPIO.output(24, False)

try:
  while True:
    time.sleep(1)

    # Send 10us pulse
    GPIO.output(24, True)
    time.sleep(0.00001)
    GPIO.output(24, False)
    start = time.time()
    while GPIO.input(22)==0:
      start = time.time()

    while GPIO.input(22)==1:
      stop = time.time()

    # Distance pulse travelled is elapsed time multiplied by the speed
    # of sound (m/s) and object must be half-way.
    elapsed = stop-start
    distance = elapsed * 340 * 0.5

    print ("Distance (m) = " + str(distance))

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
