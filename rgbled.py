#!/usr/bin/env python

"""
rgbled.py: Messing around with RGB Led on Rasberry PI
"""

import RPi.GPIO as GPIO

# Setup Pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

# Methods for Multicolor RGB
def yellow():
	GPIO.output(20, False)
	GPIO.output(21, False)

def red():
	GPIO.output(20, True)
	GPIO.output(21, False)

def green():
	GPIO.output(20, False)
	GPIO.output(21, True)

def reset():
	GPIO.output(20, True)
	GPIO.output(21, True)

def end():
	GPIO.cleanup()

# Main
reset()
green()

