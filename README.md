# weatherbot
Simple bot to pull weather and forecast info from forecast.io and tweet it.

System Requirements:
  Python 2.6+
  python-forecastio
  twitter python library
  
Other requirements:
  Twitter API keys
  DarkSky (Forecast.io) API key
  
Note: This bot was originally developed on a basic CentOS 6.7 installation. It has not been tested with anything above Python 2.6, but it's a very basic script so I see no reason why it wouldn't work. Also, I'm not a Python coder, so I'm quite certain the code is ugly and inefficient.

Installation:

First you're going to need the aforementioned python libraries. Fortunately, they install easily with pip, so...
  pip install twitter
  pip install python-forecastio
  
I'm going to assume you can handle signing up for a Darksky API key and Twitter API. If not, well, you may want to read up on them. https://developer.forecast.io/ and https://apps.twitter.com/ respectively.

Copy the weatherbot.py script to where you want it and installation is complete.

Configuration:

Here's the fun part. Figuring out what goes where.

To get forecast data, you'll need the Darksky API key for your account and the lat/long of the city you want to pull data on. I find http://citylatitudelongitude.com/ is quick and easy. Once you have that, edit the weatherbot.py to update the following fields:
  darksky_api_key
  lat
  lng
  
For some reason, the Twitter API refers to the keys and tokens via different names than what the apps.twitterlcom website use. So, here's the translation.

con_secret = Consumer Key (API Key)
con_secret_key = Consumer Secret (API Secret)
token = Access Token
token_key = Access Token Secret

That's it. Run the python script and check the resulting tweet. (You can comment out the api.statuses.update line and add a print statement if you want to see what the tweet will look like before engaging twitterland)

The Darksky API provides a lot more data that we're displaying here. If you want to make this bot your own (and you should), read through the docs and play around with the output.
