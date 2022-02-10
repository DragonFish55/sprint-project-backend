from app import db


class User(db.Model):
    __tablename__ = 'user'

    _id = db.Column("id",db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password