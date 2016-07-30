#!/usr/bin/env python
import sys
import forecastio
import datetime
from twitter import *

darksky_api_key = "YOU_NEED_DIS"
lat = DIS_TOO
lng = ALSO_DIS

time = datetime.datetime.now()

forecast = forecastio.load_forecast(api_key, lat, lng, time)

cc = forecast.currently()
currstat = cc.summary
currtemp = cc.temperature

ch = forecast.hourly()
df = ch.summary

cd = forecast.daily()
for hourlyData in cd.data:
     hitemp = hourlyData.temperatureMax

alertcast = forecastio.load_forecast(api_key, lat, lng)
existalert = alertcast.alerts()

if existalert == []:
     ca = "No current alerts"
else:
     ca = "http://bit.ly/2aoo0rb"


tweetStr = "Current conditions: %s  %dF.\nToday's forecast: %s  High: %dF.\nAlerts: %s" % (currstat, currtemp, df, hitemp, ca)

con_secret = 'Your Consumer Key (API Key)'
con_secret_key = 'Your Consumer Secret (API Secret)'
token = 'Your Access Token'
token_key = 'Your Access Token Secret'

api = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

api.statuses.update(status=tweetStr)
