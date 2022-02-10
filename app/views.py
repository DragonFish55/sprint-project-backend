from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from . import app
from models import User


#create local account
@app.route('/signup', methods = ["POST"])
def signup():
    data_in = request.get_json()
    user = data_in["username"]
    confirm_pass = data_in['confirmpass']
    password = data_in['password']
    data_out = "false"
    if(confirm_pass == password):
        userlist = User.query.filter_by(username=user)
        print(userlist)
        data_out = "true"
    else:
        data_out = "false"
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    return data_out

#signin account
@app.route('/signin', methods = ["POST"])
def signin():
    
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    data_out = "true"
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    return data_out