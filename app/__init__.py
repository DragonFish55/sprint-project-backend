
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis
from cryptography.fernet import Fernet
from http import HTTPStatus


app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SESSION_PERMANENT'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/UserData"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://iavwlxciyylzdn:1e1b50f712faafc7420dc32bf526fab7ac91de1fef02bca05fadadf7b3ba05d7@ec2-44-198-194-64.compute-1.amazonaws.com:5432/d4e00jjb3kcgf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"
Session(app)
heroku=Heroku(app)





    
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')
    

