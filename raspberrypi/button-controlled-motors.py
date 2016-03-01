"""buttons-controlled-motors.py - a GPIO circuit using momentary push buttons to control DC motors.

This drives the dual L9110 H-bridge driver GPIO circuit with two DC motors, according
to states of 4 push buttons. See l9110.md and 4-button.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

signal_pins = [4, 17, 27, 22]
control_pins = [24, 23, 25, 18]
pin_states = [False, False, False, False]

GPIO.setmode(GPIO.BCM)
for pin in signal_pins:
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)

try:
  while True:
    prev_pin_states = pin_states[0:4]
    for i in range(len(signal_pins)):
      pin_states[i] = GPIO.input(signal_pins[i]) == GPIO.LOW

    if cmp(pin_states, prev_pin_states) != 0:
      print (str(pin_states))
      for i in range(0, len(control_pins)):
        GPIO.output(control_pins[i], pin_states[i]) 

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
