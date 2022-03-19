from flask import Flask,json
import unittest
from app import app
from app.models import User, db

class SettingsUnit(unittest.TestCase):
    
    app = Flask(__name__)

    def test_settings_update_200_Add(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
            data = json.loads(resp2.get_data(as_text=True))
            resp2 = app.test_client().get("/api/" + user + "/getApiData")
        else:
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            find_user = User.query.filter_by(username=user).first()
            if(find_user is not None):
                resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=false")
                data = json.loads(resp2.get_data(as_text=True))
                resp2 = app.test_client().get("/api/" + user + "/getApiData")
        print(find_user.user_types)
        data = json.loads(resp2.get_data(as_text=True))  
        print(data)
        assert data['dataout'] != "None" 
        assert resp2.status_code == 200

    def test_settings_update_200_Rem(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
            data = json.loads(resp2.get_data(as_text=True))
            resp2 = app.test_client().get("/api/" + user + "/getApiData")
        else:
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            find_user = User.query.filter_by(username=user).first()
            if(find_user is not None):
                resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
                data = json.loads(resp2.get_data(as_text=True))
                resp2 = app.test_client().get("/api/" + user + "/getApiData")
        print(find_user.user_types)
        data = json.loads(resp2.get_data(as_text=True))  
        print(data)
        assert data['dataout'] != "None" 
        assert resp2.status_code == 200

    def test_settings_update_401(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
            data = json.loads(resp2.get_data(as_text=True))
            resp2 = app.test_client().get("/api/" + user + "/getApiData")
        else:
            resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
            find_user = User.query.filter_by(username=user).first()
            if(find_user is not None):
                resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=false")
                data = json.loads(resp2.get_data(as_text=True))
                resp2 = app.test_client().get("/api/" + user + "/getApiData")
        print(find_user.user_types)
        data = json.loads(resp2.get_data(as_text=True))  
        print(data)
        assert data['dataout'] != "None" 
        assert resp2.status_code == 200


if __name__ == "__main__":
    unittest.main()
    
   