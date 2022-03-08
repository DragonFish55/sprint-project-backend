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
CORS(app, supports_credentials=True)
#apply the headers to the app
app.config['CORS_HEADERS']='Content-Type'
app.config.from_object(__name__)
app.config['SESSION_PERMANENT'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/Users"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://wirnasaasbezcl:6f92fec655f04e1c31787b3684d6b58baae9d4a9c9ea2f178972a3364214d4f8@ec2-3-225-79-57.compute-1.amazonaws.com:5432/da6vo8aad57bna"
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
