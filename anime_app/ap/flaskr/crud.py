
from api.search_tweets import get_tweets
from models import Tweets
from app import db

# db.create_all()

# tweets = Tweets(
#     created_at='2021-07-21 02:00:00',
#     user_name='MUSE Malaysia & Brunei',
#     screen_name='@tanteiwamou_',
#     profile_img='http://pbs.twimg.com/profile_images/1380093778707447808/Tr79Gu--_normal.jpg',
#     full_text='''Ilustrasi special untuk commemorate Episode 3 《The Detective is Already Dead》
#     Source : @tanteiwamou_
#     Setiap Ahad 22:00 PM Youtube

#     (BM)
#     https://t.co/XGeGPKSik9
#     (ENG)
#     https://t.co/PD0UCUJ1vW
#     (Chinese)
#     https://t.co/cCTDXKXZCZ

#     #たんもし #TheDetectiveIsAlreadyDead #musemalaysia https://t.co/GSK67q5dzT''',
# )
# with db.session.begin(subtransactions=True):
#     db.session.add(tweets)
# db.session.commit()

query = '(#tanmoshi OR #たんもし) AND -filter:retweets AND -filter:replies -#AniList'
get_tweets(query=query, count=3)

