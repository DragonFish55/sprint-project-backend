from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate
import psycopg2

db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost/users"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://ozrbtcfskkmjvv:f8affe22e8c03cc4c12adf2ffeeae8c57e5a9c4282ac2f1e5a6854f26c495e8f@ec2-18-215-8-186.compute-1.amazonaws.com:5432/d92pkpg00p46rj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)

#define User table
class User(db.Model):
    __tablename__ = 'users_tab'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    enc_key = db.Column(db.String(1000), nullable=False)
    user_types = db.Column(db.String(1000), nullable=True)
    
    def __init__(self, username, password, enc_key, usertypes):
        self.username = username
        self.password = password
        self.enc_key = enc_key
        self.user_types = usertypes

#define Favorites table
class Favorites(db.Model):
    __tablename__ = 'fav_tab'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(1000), nullable=False)
    pub_date = db.Column(db.String(1000), nullable=True)
    desc = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(1000), nullable=False)
    source = db.Column(db.String(1000), nullable=True)
    
    def __init__(self, username, type, title, author, pub_date, desc, image, source):
        self.username = username
        self.type = type
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.desc = desc
        self.image = image
        self.source = source