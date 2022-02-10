from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from models import db
import os


app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ronexffqrugnjx:5ab471aedc41d2a7a1f8da2a0cc912c5210dfe9ff83e2d3fb71bf4fa0692f17d@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d77is03fnt6nrs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku=Heroku()


db.init_app(app)


#create local account
@app.route('/signup', methods = ["POST"])
@cross_origin()
def signup():
    data_in = request.get_json()
    confirm_pass = data_in['confirmpass']
    password = data_in['password']

    data_out = "true"
    return data_out

#signin account
@app.route('/signin', methods = ["POST"])
@cross_origin()
def signin():
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    
    data_out = "true"
    return data_out








if __name__ == "__main__":
    app.run(debug=True)