"""motion-indicator.py - detect and signal motion.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

import RPi.GPIO as GPIO
import time

array_pins = [14, 15, 18, 23, 24]

red = 14
yellow = 15
green = 18
white = 23
blue = 24

signal_pin = 4

GPIO.setmode(GPIO.BCM)
for pin in array_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, GPIO.LOW)
GPIO.setup(signal_pin, GPIO.IN)

last_motion_time = time.time()

try:
  while True:
    if GPIO.input(signal_pin):
      last_motion_time = time.time()

    current_time = time.time()

    if current_time - last_motion_time < 0.5:
      GPIO.output(red, True)
      GPIO.output(yellow, False)
      GPIO.output(green, False)
    elif current_time - last_motion_time < 3.5:
      GPIO.output(red, False)
      GPIO.output(yellow, True)
      GPIO.output(green, False)
    else:
      GPIO.output(red, False)
      GPIO.output(yellow, False)
      GPIO.output(green, True)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
