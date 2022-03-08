from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_migrate import Migrate

db=SQLAlchemy(app)
migrate = Migrate(app,db)

#define User table
class User(db.Model):
    __tablename__ = 'user'

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