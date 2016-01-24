"""morse.py - a Morse code simulator using a Raspberry Pi. 

This drives the KY-012 GPIO circuit which uses an active buzzer. See ky-012.md for details. 
This is an alternative to the Morse code circuit that the Scouts are building to practise
breadboard prototyping.
Simply type into the console, and when you hit enter, the text will be queued for output
as Morse code.

Press Ctrl+c to exit.
"""

import RPi.GPIO as GPIO
import sys
import time

print (__doc__)

buzz_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzz_pin, GPIO.OUT)

gap_time = 0.1
short_time = 0.3
medium_time = 0.7
dot_time = 0.1
dash_time = 0.3

dot = 0
dash = 1

encode = {'a':[dot, dash],
          'b':[dash, dot, dot, dot],
          'c':[dash, dot, dash, dot],
          'd':[dash, dot, dot],
          'e':[dot],
          'f':[dot, dot, dash, dot],
          'g':[dash, dash, dot],
          'h':[dot, dot, dot, dot],
          'i':[dot, dot],
          'j':[dot, dash, dash, dash],
          'k':[dash, dot, dash],
          'l':[dot, dash, dot, dot],
          'm':[dash, dash],
          'n':[dash, dot],
          'o':[dash, dash, dash],
          'p':[dot, dash, dash, dot],
          'q':[dash, dash, dot, dash],
          'r':[dot, dash, dot],
          's':[dot, dot, dot],
          't':[dash],
          'u':[dot, dot, dash],
          'v':[dot, dot, dot, dash],
          'w':[dot, dash, dash],
          'x':[dash, dot, dot, dash],
          'y':[dash, dot, dash, dash],
          'z':[dash, dash, dot, dot],
          '1':[dot, dash, dash, dash, dash],
          '2':[dot, dot, dash, dash, dash],
          '3':[dot, dot, dot, dash, dash],
          '4':[dot, dot, dot, dot, dash],
          '5':[dot, dot, dot, dot, dot],
          '6':[dash, dot, dot, dot, dot],
          '7':[dash, dash, dot, dot, dot],
          '8':[dash, dash, dash, dot, dot],
          '9':[dash, dash, dash, dash, dot],
          '0':[dash, dash, dash, dash, dash],
          '.':[dot, dash, dot, dash, dot, dash],
          '?':[dot, dot, dash, dash, dot, dot],
          }
try:
  while True:
    message = sys.stdin.readline()
    for character in message:
      print ('> ' + character)
      if character == ' ':
        time.sleep(medium_time)
      elif character in encode:
        time.sleep(short_time)
        for bleep in encode[character]:
            time.sleep(gap_time)
            GPIO.output(buzz_pin, True)
            if bleep == dot:
              time.sleep(dot_time)
              print ('dot')
            else:
              time.sleep(dash_time)
              print ('dash')
            GPIO.output(buzz_pin, False)
      else:
        print ('> ?')

except KeyboardInterrupt:
  GPIO.cleanup()

except Exception as e:
  print (str(e))
  GPIO.cleanup()
