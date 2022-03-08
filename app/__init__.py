from flask import Flask
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

#initialize flask app
app = Flask(__name__)
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

#enable CORS
CORS(app, supports_credentials=True)
#apply the headers to the app
app.config['CORS_HEADERS']='Content-Type'
app.config.from_object(__name__)
app.config['SESSION_PERMANENT'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SESSION_COOKIE_NAME'] = "def_session"
app.secret_key = "secret"

#initialize session an heroku
session_app = Session(app)
heroku=Heroku(app)
session_app.init_app(app)

#import views
from app import views
