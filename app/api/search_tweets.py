
import json
import datetime, time, sys
import config
import pandas as pd
from abc import ABCMeta, abstractmethod
from tqdm import tqdm
from dateutil.parser import parse
from requests_oauthlib import OAuth1Session
from pprint import pprint

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"

query = '(#tanmoshi OR #たんもし) AND -filter:retweets AND -filter:replies -#AniList'
params = {
          'q': query,
          'count': 5,
          'lang': 'en',
          }

res = twitter.get(url, params=params)
# json形式でloadしないと認識できない
timelines = json.loads(res.text)
# pprint(timelines)
for line in timelines['statuses']:
	print(line['created_at'])
	print(line['user']['name'])
	print(line['user']['screen_name'])
	print(line['user']['profile_image_url'])
	print(line['full_text'])
	print('\n')
	try:
		medias = line['extended_entities']['media']
		for media in medias:
			print(media['media_url'])
	except:
		pass
	print('----------------')





