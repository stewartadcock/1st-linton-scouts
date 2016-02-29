"""4-buttons.py - a GPIO circuit with for momentary push buttons.

See 4-button.md for details.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import time

print (__doc__)

signal_pins = [4, 17, 27, 22]
pin_states = [False, False, False, False]

GPIO.setmode(GPIO.BCM)
for pin in signal_pins:
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
  while True:
    prev_pin_states = pin_states[0:4]
    for i in range(len(signal_pins)):
      pin_states[i] = GPIO.input(signal_pins[i]) == GPIO.LOW

    if cmp(pin_states, prev_pin_states) != 0:
      print (str(pin_states))

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
