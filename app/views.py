#from flask import Flask, Response, request, jsonify
#from flask_cors import CORS, cross_origin
#from app import app
from models import User,db
from app import app
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy

from flask_session import Session
from flask_redis import FlaskRedis
from cryptography.fernet import Fernet
from app.models import User
from app.src import *
from http import HTTPStatus

db.init_app(app)

@app.route('/api/home', methods = ["GET"])
@cross_origin()
def home():
    username = ""
    if "username" in session:
        username = session['username']
        jsonify({"username":username})


@app.route('/api/logout', methods = ["POST"])
@cross_origin()
def logout():
    session.pop('username',None)
    return jsonify({"data_out":"to_login"})

#create account
@app.route('/api/signup', methods = ["POST"])
@cross_origin()
def signup():
    data_out = 'false'
    data_in = request.get_json()
    user = data_in["username"]
    password = data_in['password']
    find_user = User.query.filter_by(username=user).first()
    if(find_user is None):
        enc_key = Fernet.generate_key()
        enc_key_dec = enc_key.decode()
        fernet_var = Fernet(enc_key)
        encrypted_pass = fernet_var.encrypt(password.encode())
        firstpass = encrypted_pass.decode()
        new_user = User(username=user,password=firstpass,enc_key=enc_key_dec)
        db.session.add(new_user)
        db.session.commit()
        data_out = "true"    
    return jsonify({'data_out':data_out})
    

#signin account
@app.route('/api/signin', methods = ["POST"])
@cross_origin()
def signin():
    data_out = 'false'
    encrypt_pass = ""
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    find_user = User.query.filter_by(username=user).first()
    if(find_user is not None):
        session["username"] = user
        enc_key = find_user.enc_key
        enc_key = enc_key.encode()
        fernet_var = Fernet(enc_key)
        saved_pass = find_user.password
        encrypt_pass = fernet_var.decrypt(saved_pass.encode()).decode()
        if(password == encrypt_pass):
            data_out = "true"
    return jsonify({'data_out':data_out})

with app.app_context():
    db.create_all()
'''

#create local account
@app.route('/api/signup', methods = ["POST"])
@cross_origin(supports_credentials=True)
def signup(params):
    
    
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
    
    data_out = jsonify({"hi":"thre"})
    data_out.headers.set('Access-Control-Allow-Origin', '*')
    data_out.headers.set('Access-Control-Allow-Headers', '*')
    data_out.headers.set('Access-Control-Allow-Methods', '*')
    data_out.headers.set('Access-Control-Allow-Credentials', '*')


    return data_out

#signin account
@app.route('/api/signin', methods = ["POST"])
@cross_origin(supports_credentials=True)
def signin():
    
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    data_out = "true"
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    data_out.headers.add('Access-Control-Allow-Headers', '*')
    data_out.headers.add('Access-Control-Allow-Methods', '*')
    return jsonify(data_out)
'''