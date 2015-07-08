#!/usr/bin/env python

"""
weather.py: check weather with wunderground api
"""

# from rgbled import *
from urllib2 import Request, urlopen, URLError
import json
import logging

city = "new_york"
state = "new_york"
with open('keys.json','r') as keyfile:
    api_key = json.load(keyfile)['wunderground_api']
url = "http://api.wunderground.com/api/%s/forecast/q/%s/%s.json" % (api_key, city, state)

def query_api(query_url):
    request = Request(query_url)
    try:
        response = urlopen(request)
        response_json = json.loads(response.read())
        return response_json
    except URLError, e:
        print 'Got an error code:', e

def rain():
    """
    returns true if it is going to rain today and false if it is not.
    """
    try:
        weather = query_api(url)
        forecast = weather['forecast']['simpleforecast']['forecastday'][0]
        date = forecast['date']['pretty']
        qpf_allday = float(forecast['qpf_allday']['in'])
        if qpf_allday > 0.0:
            return True
        return False
    except:
        raise Exception('There was an error in parsing the response from the API.')
