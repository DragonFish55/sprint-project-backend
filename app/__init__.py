from flask import Flask, Response, request,jsonify
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from cryptography.fernet import Fernet

app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://MainUserNew:happysquash@localhost:5432/UserData"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ronexffqrugnjx:5ab471aedc41d2a7a1f8da2a0cc912c5210dfe9ff83e2d3fb71bf4fa0692f17d@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d77is03fnt6nrs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db=SQLAlchemy(app)
migrate = Migrate(app,db)
app.secret_key = "secret"
heroku=Heroku(app)
db.init_app(app)



class User2(db.Model):
    __tablename__ = 'user2'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    enc_key = db.Column(db.String(1000), nullable=False)
    

    def __init__(self, username, password, enc_key):
        self.username = username
        self.password = password
        self.enc_key = enc_key
        

#create local account
@app.route('/api/signup', methods = ["POST"])
@cross_origin()
def signup():
    data_in = request.get_json()
    print(data_in)
    
    user = data_in["username"]
    confirm_pass = data_in['confirmpass']
    password = data_in['password']
    data_out = "false"
    if(confirm_pass == password):
        find_user = User2.query.filter_by(username=user).first()
        if(find_user is None):
            enc_key = Fernet.generate_key()
            enc_key_dec = enc_key.decode()
            fernet_var = Fernet(enc_key)
            encrypted_pass = fernet_var.encrypt(password.encode())
            new_user = User2(username=user,password=encrypted_pass,enc_key=enc_key_dec)
            db.session.add(new_user)
            db.session.commit()
        else:
            data_out = "false"
    else:
        data_out = "false"
    
    data_out = jsonify({"hi":"thre"})
    

    return data_out

#signin account
@app.route('/api/signin', methods = ["POST"])
@cross_origin()
def signin():
    decrypt_pass = ''
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    print(password)

    find_user = User2.query.filter_by(username=user).first()
    print('hi')
    if(find_user is not None):
        enc_key = find_user.enc_key
        print('there')
        saved_pass = find_user.password
        print(enc_key)
        fernet_var = Fernet(enc_key)
        print('bye')
        decrypt_pass = fernet_var.decrypt(saved_pass)
        print('fly')
        if(password == decrypt_pass):
            print("they are equal")
    print(decrypt_pass)
    print(password)
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')
    data_out = "true"
    return data_out

with app.app_context():
    db.create_all()