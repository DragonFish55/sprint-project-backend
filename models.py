#from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import app


db=SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return "{'username': " + self.username + ", 'password':" + self.password + "}"