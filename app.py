from flask import Flask, Response, request, jsonify
from flask_cors import CORS, cross_origin
from flask_heroku import Heroku
from models import *



dbname="postgresql-rectangular-42071"
app=Flask(__name__)
app['SECRET_KEY'] = 'scret'
CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/" + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku=Heroku()

#migrate=Migrate()
db.init_app(app)
#migrate.init_app(app,db)
db.create_all()

#create local account
@app.route('/signup', methods = ["POST"])
@cross_origin()
def signup():
    data_in = request.get_json()
    confirm_pass = data_in['confirmpass']
    password = data_in['password']

    data_out = "true"
    return data_out

#signin account
@app.route('/signin', methods = ["POST"])
@cross_origin()
def signin():
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    
    data_out = "true"
    return data_out


def validateSignup(dataobj):
    dataobj






if __name__ == "__main__":
    app.run(debug=True)