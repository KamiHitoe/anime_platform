
from app import app
from models import Tweets
from flask import render_template

@app.route('/index')
def index():
    tweets = Tweets.query.order_by(Tweets.id).all()
    return render_template('index.html', tweets=tweets)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')


