
from urllib import response
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_redis import FlaskRedis
from cryptography.fernet import Fernet
from http import HTTPStatus

#initialize the flask app component
app=Flask(__name__)
#enable CORS
CORS(app)
#apply the headers to the app
app.config['CORS_HEADERS']='Content-Type'
app.config['SESSION_PERMANENT'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost/users"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://wirnasaasbezcl:6f92fec655f04e1c31787b3684d6b58baae9d4a9c9ea2f178972a3364214d4f8@ec2-3-225-79-57.compute-1.amazonaws.com:5432/da6vo8aad57bna"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"

#create migration,session, and heroku component
Session(app)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
heroku=Heroku(app)
db.init_app(app)

#define User table
class User(db.Model):
    __tablename__ = 'users_tab'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    enc_key = db.Column(db.String(1000), nullable=False)
    

    def __init__(self, username, password, enc_key):
        self.username = username
        self.password = password
        self.enc_key = enc_key

#defines the signup api endpoint
@app.route('/api/signup', methods = ["POST"])
@cross_origin()
def signup():
    #get incoming json data
    response_code = 200
    data_out = 'false'
    data_in = request.get_json()
    user = data_in["username"]
    password = data_in['password']
    #if username is in database generate encrypted key and
    #create new user otherwise signup failed and output 401
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
    else:
        response_code = 401

    return jsonify({'data_out':data_out}),response_code
    

#defines the signin api endpoint
@app.route('/api/signin', methods = ["POST"])
@cross_origin()
def signin():
    response_code = 200
    user_err = "false"
    pass_err = "false"
    encrypt_pass = ""
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    #if user is in database table decrypt the table password
    #and if the passwords match return 200 ok otherwise return 401
    find_user = User.query.filter_by(username=user).first()
    print(find_user)
    if(find_user is not None):
        user_err = "false"
        #session["username"] = user
        enc_key = find_user.enc_key
        enc_key = enc_key.encode()
        fernet_var = Fernet(enc_key)
        saved_pass = find_user.password
        encrypt_pass = fernet_var.decrypt(saved_pass.encode()).decode()
        if(password == encrypt_pass):
            pass_err = "false"
            response_code = 200
        else:
            pass_err = "true"
            response_code = 401  
    else:
        user_err = "true"
        pass_err = "true"
        response_code = 401
    return jsonify({'user_error':user_err, "pass_error":pass_err}),response_code
    
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')


#signout api
@app.route('/api/signout', methods = ["POST"])
@cross_origin()
def signout():
    response_code = 200
    data_out = "false"
    data_in = request.get_json()
    user = data_in['username']
    #if user in table then respond 200 otherwise respond 404
    #also signal user to logout if ok
    find_user = User.query.filter_by(username=user).first()
    if(find_user is not None):
        data_out = "true"
        response_code = 200
    else:
        response_code = 404
    return jsonify({'user_error':data_out}),response_code

#create app tables
with app.app_context():
    db.create_all()