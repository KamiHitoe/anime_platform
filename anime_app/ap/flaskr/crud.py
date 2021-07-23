
from api.search_tweets import get_tweets
from models import Tweets
from app import db

# db.create_all()

query = '(#tanmoshi OR #たんもし) AND -filter:retweets AND -filter:replies -#AniList'
tweets_dic_list = get_tweets(query=query, count=10)
for tweets_dic in tweets_dic_list:
    tweet = Tweets(
        tweets_dic['created_at'],
        tweets_dic['user_name'],
        tweets_dic['screen_name'],
        tweets_dic['profile_img'],
        tweets_dic['full_text'],
    )
    with db.session.begin(subtransactions=True):
        db.session.add(tweet)
    db.session.commit()


