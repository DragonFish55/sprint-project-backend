from flask import Flask,json
import pytest
import unittest
from app import app
from app.models import User, db

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
        assert resp.status_code == 200
        data = json.loads(resp.get_data(as_text=True))
        assert data['data_out'] != "false"
        find_user = User.query.filter_by(username=user).first()

    # Test that given any username and password the user is added
    # to the database successfully
    def test_signup_401(self):
        user = "mush"
        password = "hats1fhdfggfx"
        find_user = User.query.filter_by(username=user).first()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        if(find_user is None):
            resp2 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            assert resp2.status_code == 401
            data = json.loads(resp2.get_data(as_text=True))
            assert data['data_out'] == "false"
        else:
            assert resp1.status_code == 401
            data = json.loads(resp2.get_data(as_text=True))
            assert data['data_out'] != "false"

        assert data['data_out'] != "false"

if __name__ == "__main__":
    unittest.main()