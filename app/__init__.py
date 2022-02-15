
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_redis import FlaskRedis
from cryptography.fernet import Fernet
from app.models import User
from app.src import *
from http import HTTPStatus


app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SESSION_PERMANENT'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/UserData"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ronexffqrugnjx:5ab471aedc41d2a7a1f8da2a0cc912c5210dfe9ff83e2d3fb71bf4fa0692f17d@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d77is03fnt6nrs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"
Session(app)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
heroku=Heroku(app)
db.init_app(app)



@app.route('/api/logout', methods = ["POST"])
@cross_origin()
def logout():
    return "hi"


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
        #print(encrypt_pass)
        if(password == encrypt_pass):
            #session = Session.query.filter_by(id=find_user.id)
           
                #session.sessionid = 
                #print("they are equal")
                #find_user.sessionid = 
            data_out = "true"
    return jsonify({'data_out':data_out})
    
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')
    

with app.app_context():
    db.create_all()