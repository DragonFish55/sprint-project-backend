from flask import Flask,json
import unittest
from app import app
from app import User, db

class SettingsUnit(unittest.TestCase):
    
    app = Flask(__name__)

    def test_settings_update_200_Add(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        teststring = "Health"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?" + teststring + "=true")
            find_user = User.query.filter_by(username=user).first()
            if(teststring in find_user.user_types):
                found = 1
        assert found == 1

    def test_settings_update_200_Rem(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        teststring = "Health"

        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?" + teststring + "=true")
            find_user = User.query.filter_by(username=user).first()
            if(teststring in find_user.user_types):
                resp2 = app.test_client().get( "/api/new/" +  user + "/categories?" + teststring + "=false")
                find_user = User.query.filter_by(username=user).first()
                if(teststring not in find_user.user_types):
                    found = 1
        assert found == 1
        
    def test_settings_update_401(self):
        user="user1"
        data = None
        resp1 = None
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
        data = json.loads(resp1.get_data(as_text=True))

        assert data["dataout"] == "false"
        assert resp1.status_code == 401

if __name__ == "__main__":
    unittest.main()
    
   