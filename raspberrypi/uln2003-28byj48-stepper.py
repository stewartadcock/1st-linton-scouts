"""uln2003-28byj48-stepper.py - demo script for ULN2003 GPIO circuit with a 28BYJ-48 stepper motor.

See uln2003-28bjy48-stepper.md for details. 

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

control_pins = [6, 13, 19, 26]

# This sequence is suggested in the manufacturers datasheet
sequence = [[1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1],
            [1,0,0,1]]

GPIO.setmode(GPIO.BCM)
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

step_time = 0.002

pos = 0
step = 1

try:
  while True:
 
    for pin in range(0,4):
      GPIO.output(control_pins[pin], sequence[pos][pin])
 
    pos += step

    if pos >= len(sequence):
      pos = 0

    time.sleep(step_time)

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
