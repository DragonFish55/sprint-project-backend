from flask import Flask, Response, request
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy



db=SQLAlchemy()
app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ronexffqrugnjx:5ab471aedc41d2a7a1f8da2a0cc912c5210dfe9ff83e2d3fb71bf4fa0692f17d@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d77is03fnt6nrs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
heroku=Heroku(app)
db.init_app(app)
with app.app_context():
    db.create_all()
