
from flask import Flask, Response, render_template, request,jsonify, session
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_session import Session
from flask_redis import FlaskRedis
from cryptography.fernet import Fernet
from http import HTTPStatus


app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SESSION_PERMANENT'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/Users"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://xreaevalhltowj:0ff5ecb8305bba2528cc958710e990c441ddc0295cb7ed4cff95c42c108ea70a@ec2-18-215-8-186.compute-1.amazonaws.com:5432/d11neo5i1fqjgt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"
Session(app)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
heroku=Heroku(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    enc_key = db.Column(db.String(1000), nullable=False)
    

    def __init__(self, username, password, enc_key):
        self.username = username
        self.password = password
        self.enc_key = enc_key


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
    
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')
    

with app.app_context():
    db.create_all()