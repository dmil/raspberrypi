#!/usr/bin/env python

"""
main.py - turns light red if I might need an umbrella today, and green if I won't
"""

import rain from weather
import rgbled

if rain():
    rgbled.red()
else:
    rgbled.green()

