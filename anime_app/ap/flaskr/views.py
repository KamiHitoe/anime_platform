
from app import app
from models import Users
from flask import render_template

@app.route('/index')
def index():
    users = Users.query.order_by(Users.id).all()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
