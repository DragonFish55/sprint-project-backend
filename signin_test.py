from urllib import response
from django.test import LiveServerTestCase
from flask import jsonify
import flask_unittest
import flask.globals
from sqlalchemy import delete
import urllib3
from app import app
import unittest
from flask import json
from flask import Flask

#from app.models import User
'''
class Test(LiveServerTestCase):
    def createapp(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8000
        app.config['LIVESERVER_TIMEOUT'] = 15
        return app
    def test1(self):
        http = urllib3.PoolManager()
        resp = http.request('POST', '/api/signup')
  '''      

class TestUnit(unittest.TestCase):
    
    app = app

    #test signup user into db
    def test_signup(self):
            
        user = "mush"
        password = "hats1fhdfggfx"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        assert resp.status_code == 200
        data = json.loads(resp.get_data(as_text=True))
        assert data['data_out'] != "false"
        find_user = User.query.filter_by(username=user).first()
        assert find_user != None

    def test_signin(self):
        user = "mush"
        password = "hats1fhdfggfx"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is None):
            resp = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp = app.test_client().post('/api/signin',
                                        data=json.dumps({"username":user,"password":password}),
                                        content_type='application/json')
            assert resp.status_code == 200
            data = json.loads(resp.get_data(as_text=True))
            assert data['data_out'] != "false"
            find_user = User.query.filter_by(username=user).first()
            assert find_user != None
        else:
            return "error signing in"
        
    #check for 200 okay
    def test_ok(self):
           
        url = ''
        user="user1"
        password="pass1"
        resp = app.test_client().post('http://127.0.0.1:5000/api/signin',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
       
        data = json.loads(resp.get_data(as_text=True))
        assert resp.status_code == 200
        

if __name__ == "__main__":
    #app.run(debug=True)
    #print("hi")
    unittest.main()
    