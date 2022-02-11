from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from app import app
from models import User


CORS(app, resources={r"/api/*":{"origins":"*"}})
app.config['CORS_HEADERS']='Content-Type'

#create local account
@app.route('/api/signup', methods = ["POST"])
def signup():
    data_in = request.get_json()
    '''
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
    
    '''
    data_out = jsonify(data_out)
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    data_out.headers.add('Access-Control-Allow-Headers', '*')
    data_out.headers.add('Access-Control-Allow-Methods', '*')

    return data_out

#signin account
@app.route('/api/signin', methods = ["POST"])
def signin():
    
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    data_out = "true"
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(data_out)