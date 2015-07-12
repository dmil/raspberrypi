#!/usr/bin/env python

"""
relay.py: Relay
"""

import RPi.GPIO as GPIO
import time

# Setup Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

for i in range(10):
	time.sleep(2)
	print "HIGH"
	GPIO.output(18, GPIO.HIGH)
	
	time.sleep(2)
	print "LOW"
	GPIO.output(18, GPIO.LOW)

GPIO.cleanup()