from flask import Flask,json
import unittest
from app import app
from app import User, db

class SigninUnit(unittest.TestCase):
    
    app = Flask(__name__)

    # Test that given any username and password the user is added
    # to the database successfully
    def test_signin_200_pass_match(self):
            
        user = "mush"
        password = "hats1fhdfggfx"
        resp2 = None
        data = None
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().post('/api/signin',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            data = json.loads(resp2.get_data(as_text=True))
            assert resp2.status_code == 200        
            assert data['user_error'] == "false"
            assert data['pass_error'] == "false"

    # Test that given any username and password the password
    # is invalid even though the username exists
    def test_signin_401_pass_error(self):
            
        user = "mush"
        password = "hats1fhdfggfx"
        passinvalid = "hey"
        resp2 = None
        data = None
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().post('/api/signin',
                                    data=json.dumps({"username":user,"password":passinvalid}),
                                    content_type='application/json')
            data = json.loads(resp2.get_data(as_text=True))
            assert resp2.status_code == 401       
            assert data['user_error'] == "false"
            assert data['pass_error'] == "true"

    # Test that given a user that isnt in the database a 401 
    # invalid user is returned
    def test_signin_401(self):
        user = "mush"
        password = "hats1fhdfggfx"
        data = None

        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signin',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        data = json.loads(resp1.get_data(as_text=True))
        assert resp1.status_code == 401    
        assert data['user_error'] == "true"
        assert data['pass_error'] == "true"

if __name__ == "__main__":
    unittest.main()