from flask import Flask,json
import unittest
from app import app
from app import User, db

class SignupUnit(unittest.TestCase):
    
    app = Flask(__name__)

    # Test that given any username and password the user is added
    # to the database successfully
    def test_signup_200(self):
            
        user = "mush"
        password = "hats1fhdfggfx"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        data = json.loads(resp.get_data(as_text=True))
        assert resp.status_code == 200
        assert data['data_out'] == "true"

    # Test that given any username and password the user is added
    # to the database successfully
    def test_signup_401(self):
        user = "mush"
        password = "hats1fhdfggfx"
        data = None
        resp2 = None
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            data = json.loads(resp2.get_data(as_text=True))
            assert data['data_out'] == "false"
            assert resp2.status_code == 401

if __name__ == "__main__":
    unittest.main()