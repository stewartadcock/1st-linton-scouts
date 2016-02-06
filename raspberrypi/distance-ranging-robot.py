"""distance-ranging-robot.py - an ultrasonic distance ranger robot.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

trigger_pin = 17
echo_pin = 27

SPEED_OF_SOUND = 343.2 # in dry air at 20 degrees C, 1 atm.

min_distance = 0.6
max_distance = 0.8
limit_distance = 20.0

control_pins = [24, 23, 25, 18]

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

GPIO.output(trigger_pin, False)

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

time.sleep(1)

try:
  while True:
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
    elapsed = stop - start
    distance = elapsed * SPEED_OF_SOUND * 0.5
    distance = 0.01 * int(distance*100)

    print ("Distance (m) = {:.2f}".format(distance))

    if distance > max_distance and distance < limit_distance:
      control = [0,1,0,1]
    elif distance < min_distance:
      control = [1,0,1,0]
    else:
      control = [0,0,0,0]

    for pin in range(0, len(control_pins)):
      GPIO.output(control_pins[pin], control[pin]) 

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
