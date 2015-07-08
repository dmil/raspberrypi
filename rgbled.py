#!/usr/bin/env python

"""
rgbled.py: Messing around with RGB Led on Rasberry PI
"""

# Setup Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# Methods for Multicolor RGB
def yellow():
  print("Turn light Yellow")
  GPIO.output(20, False)
  GPIO.output(21, False)

def red():
  print("Turn light Red")
  GPIO.output(20, True)
  GPIO.output(21, False)

def green():
  print("Turn light Green")
  GPIO.output(20, False)
  GPIO.output(21, True)

def end():
  print("Reset RGB pins")
  GPIO.cleanup()

# Main
if __name__ == '__main__':
    reset()
    green()

