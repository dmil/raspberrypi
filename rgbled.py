#!/usr/bin/env python

"""
rgbled.py: Messing around with RGB Led on Rasberry PI
"""

import RPi.GPIO as GPIO
import time

# Setup Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# Methods for Multicolor RGB
def yellow():
  print("Turn light Yellow")
  GPIO.output(20, GPIO.LOW)
  GPIO.output(21, GPIO.LOW)

def red():
  print("Turn light Red")
  GPIO.output(20, GPIO.HIGH)
  GPIO.output(21, GPIO.LOW)

def green():
  print("Turn light Green")
  GPIO.output(20, GPIO.LOW)
  GPIO.output(21, GPIO.HIGH)

def on():
  print("Turn light on")
  GPIO.output(19, GPIO.HIGH)
  GPIO.output(20, GPIO.HIGH)
  GPIO.output(21, GPIO.HIGH)

def off():
  print("Turn light off")
  GPIO.output(19, GPIO.LOW)
  GPIO.output(20, GPIO.HIGH)
  GPIO.output(21, GPIO.HIGH)

def cleanup():
  print("Reset RGB pins")
  GPIO.cleanup()

# Main
if __name__ == '__main__':
    on()
    green()
    time.sleep(10)
    off()
    cleanup()

