
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
	tweets_dic_list = []
	for line in timelines['statuses']:
		tweets_dic = {}
		tweets_dic['created_at'] = line['created_at']
		tweets_dic['user_name'] = line['user']['name']
		tweets_dic['screen_name'] = '@'+line['user']['screen_name']
		tweets_dic['profile_img'] = line['user']['profile_image_url']
		tweets_dic['full_text'] = line['full_text']
		media_list = []
		try:
			medias = line['extended_entities']['media']
			for media in medias:
				media_list.append(media['media_url'])
		except:
			pass
		tweets_dic['imgs'] = media_list
		tweets_dic_list.append(tweets_dic)
	print(tweets_dic_list)
	return tweets_dic_list

# get_tweets(query=query, count=3)



