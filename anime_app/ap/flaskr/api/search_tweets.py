
import api.config as config
import json
import datetime, time, sys
from abc import ABCMeta, abstractmethod
from requests_oauthlib import OAuth1Session
from pprint import pprint
# from dateutil.parser import parse

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/search/tweets.json?tweet_mode=extended"

def get_tweets(query, count):
	params = {
			'q': query,
			'count': count,
			'lang': 'en',
			}
	res = twitter.get(url, params=params)
	# json形式でloadしないと認識できない
	timelines = json.loads(res.text)
	# pprint(timelines)
	for line in timelines['statuses']:
		print('created_at:', line['created_at'])
		print('user_name:', line['user']['name'])
		print('@{}'.format(line['user']['screen_name']))
		print('profile_img:', line['user']['profile_image_url'])
		print(line['full_text'])
		print('\n')
		try:
			medias = line['extended_entities']['media']
			for media in medias:
				print('imgs:', media['media_url'])
		except:
			pass
		print('----------------')

# get_tweets(query=query, count=3)



