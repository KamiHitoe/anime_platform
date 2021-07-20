
from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask Application
app = Flask(__name__)

# Set Config Class
app.config.from_object(Config)

# Set DB
db = SQLAlchemy(app)
