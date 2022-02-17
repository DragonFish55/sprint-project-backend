from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db=SQLAlchemy()

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