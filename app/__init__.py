from urllib import response
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_session import Session
from flask_redis import FlaskRedis
from http import HTTPStatus
from app import usersettings
from datetime import timedelta

#initialize flask app
app = Flask(__name__)
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

#enable CORS
CORS(app, supports_credentials=True, expose_headers=["set-cookie"])
#apply the headers to the app
app.config['CORS_HEADERS']='Content-Type'
app.config.from_object(__name__)
app.config['SESSION_PERMANENT'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/Users"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ozrbtcfskkmjvv:f8affe22e8c03cc4c12adf2ffeeae8c57e5a9c4282ac2f1e5a6854f26c495e8f@ec2-18-215-8-186.compute-1.amazonaws.com:5432/d92pkpg00p46rj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SESSION_COOKIE_NAME'] = "def_session"
app.secret_key = "secret"

#initialize session an heroku
session_app = Session(app)
heroku=Heroku(app)
session_app.init_app(app)

#import views
from app import views
