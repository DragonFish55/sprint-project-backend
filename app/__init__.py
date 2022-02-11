from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from .models import User

app=Flask(__name__)
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ronexffqrugnjx:5ab471aedc41d2a7a1f8da2a0cc912c5210dfe9ff83e2d3fb71bf4fa0692f17d@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d77is03fnt6nrs"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate = Migrate(app,db)
app.secret_key = "secret"
heroku=Heroku(app)
db.init_app(app)

class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

#create local account
@app.route('/api/signup', methods = ["POST"])
@cross_origin()
def signup():
    data_in = jsonify({'data':'nane'})
    data_in.headers.add('Access-Control-Allow-Origin', '*')
    data_in.headers.add('Access-Control-Allow-Headers', '*')
    data_in.headers.add('Access-Control-Allow-Methods', '*')
    print(data_in)
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
    #data_out = jsonify(data_out)
    

    return data_in

#signin account
@app.route('/api/signin', methods = ["POST"])
@cross_origin()
def signin():
    
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    data_out = "true"
    data_out.headers.add('Access-Control-Allow-Origin', '*')
    data_out.headers.add('Access-Control-Allow-Headers', '*')
    data_out.headers.add('Access-Control-Allow-Methods', '*')
    return jsonify(data_out)


with app.app_context():
    db.create_all()