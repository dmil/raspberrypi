#!/usr/bin/env python

"""
main.py - turns light red if I might need an umbrella today, and green if I won't
"""

from weather import rain
import rgbled

import RPi.GPIO as GPIO
import time

import rgbled
from weather import rain

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(26)
    if input_state == True:
        print('Button Pressed')
	rgbled.on()
	if rain():
    		rgbled.red()
	else:
    		rgbled.green()
	
	time.sleep(20)
    	rgbled.off()
rgbled.cleanup()
