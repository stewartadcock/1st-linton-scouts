"""hc-sr04.py - demo script for HC-SR04 GPIO circuit - an ultrasonic distance ranger.

See hc-sr04.md for details. 

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

trigger_pin = 17
echo_pin = 27

SPEED_OF_SOUND = 343.2 # in dry air at 20 degrees C, 1 atm.

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

GPIO.output(trigger_pin, False)

try:
  while True:
    time.sleep(1)

    # Send 10us pulse
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)
    start = time.time()
    while not GPIO.input(echo_pin):
      start = time.time()

    while GPIO.input(echo_pin):
      stop = time.time()

    # Distance pulse travelled is elapsed time multiplied by the speed
    # of sound (m/s) and object must be half-way.
    elapsed = stop-start
    distance = elapsed * SPEED_OF_SOUND * 0.5
    distance = 0.01 * int(distance*100)

    print ("Distance (m) = {:.2f}".format(distance))

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
