# RandomVoat - Twitter Bot
# Tweets randomly selected post titles scraped from various subverses

from twython import Twython, TwythonError
import time
import RandomTitles

KEYS = [line.rstrip('\n') for line in open('/home/pi/RandomVoat/keys.txt')]

# Twitter keys/authentification tokens - (pulled from local .txt)
APP_KEY = KEYS[0]
APP_SECRET = KEYS[1]
OAUTH_TOKEN = KEYS[2]
OAUTH_TOKEN_SECRET = KEYS[3]

twitter_api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# Sets post content -> return value of RandomTitles.py
status = RandomTitles.main()

# Post content - Twitter
twitter_api.update_status(status=status)
