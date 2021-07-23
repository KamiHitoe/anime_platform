
from app import db
from sqlalchemy import desc

class Users(db.Model):
    """ Users Table Model
    これは後でユーザログイン機能つけた時に作りこむ予定
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Tweets(db.Model):
    """ Tweets Table Model """
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True) # AUTO INCREMENT
    created_at = db.Column(db.DateTime)
    user_name = db.Column(db.String(64))
    screen_name = db.Column(db.String(64))
    profile_img = db.Column(db.Text)
    full_text = db.Column(db.Text)
    img1 = db.Column(db.Text, nullable=True)
    img2 = db.Column(db.Text, nullable=True)
    img3 = db.Column(db.Text, nullable=True)
    img4 = db.Column(db.Text, nullable=True)

    def __init__(self, created_at, user_name, screen_name, profile_img, full_text):
        self.created_at = created_at
        self.user_name = user_name
        self.screen_name = screen_name
        self.profile_img = profile_img
        self.full_text = full_text

    @classmethod
    def select_latest_tweet(cls):
        return cls.query.order_by(desc(cls.id)).first()


