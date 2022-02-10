from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from app import app

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