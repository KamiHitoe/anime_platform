
from api.search_tweets import get_tweets
from models import Tweets
from app import db

# db.create_all()

query = '(#tanmoshi OR #たんもし) AND -filter:retweets AND -filter:replies -#AniList'
tweets_dic_list = get_tweets(query=query, count=100)
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
    # 一番下のレコードのidを取得
    if tweets_dic['imgs']:
        latest_tweet = Tweets.select_latest_tweet()
        with db.session.begin(subtransactions=True):
            for i in range(len(tweets_dic['imgs'])):
                if i == 0:
                    latest_tweet.img1 = tweets_dic['imgs'][i]
                elif i == 1:
                    latest_tweet.img2 = tweets_dic['imgs'][i]
                elif i == 2:
                    latest_tweet.img3 = tweets_dic['imgs'][i]
                elif i == 3:
                    latest_tweet.img4 = tweets_dic['imgs'][i]
        db.session.commit()




