from flask import Flask, session
from config import Config
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
SESSION_TYPE = 'redis'
app.config.from_object(Config)
login = LoginManager(app)
session = Session(app)

from app import routes
