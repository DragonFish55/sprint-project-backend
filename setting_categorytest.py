from flask import Flask,json
import unittest
from app import app
from app.models import User, db

class CategoryUnit(unittest.TestCase):
    
    app = Flask(__name__)

    # Test driven development test    
    # check that retrieving category info gives invalid 
    # user authentication
    def test_category_401(self):
           
        user="user1"
        password="pass1"
        found = 0
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp2 = app.test_client().get('/api/' + user + '/getApiData')
        data = json.loads(resp2.get_data(as_text=True))
        
        assert resp2.status_code == 401
        assert data['dataout'] == "None" 
            
        
    # Test driven development test 
    # check that retrieving category info gives valid 
    # user authentication and retrieves categories or 
    # sends back none
    def test_category_200_none(self):
        user="user1"
        password="pass1"
        resp2 = None
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
            
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            resp2 = app.test_client().get("/api/" + user + "/getApiData")
            data = json.loads(resp2.get_data(as_text=True))  
            assert data['dataout'] == "None" 
            assert resp2.status_code == 200
        

    # Test driven development test 
    # check that retrieving category info gives valid 
    # user authentication and retrieves categories or 
    # sends back none
    def test_category_200_exists(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        data = None
        resp3 = None
        
        find_user1 = User.query.filter_by(username=user).first()
        if(find_user1 is not None):
            find_user1 = User.query.filter_by(username=user).delete()
       
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        find_user2 = User.query.filter_by(username=user).first()
        if(find_user2 is not None):
            resp2 = app.test_client().get( "/api/new/" +  user + "/categories?Technology=true")
            resp3 = app.test_client().get("/api/" + user + "/getApiData")
            data = json.loads(resp3.get_data(as_text=True))  
            print(data)
            assert data['dataout'] != "None" 
            assert resp3.status_code == 200
        

    # Test driven development test 
    # Tests whether requesting the default category api using the top_headline
    # entry parameter will return top headline general data
    def test_default_200(self):
        resp2 = None
        entry = "top_headline"
        resp2 = app.test_client().get("/api/" + entry + "/defaultApi")
        data = json.loads(resp2.get_data(as_text=True))  
        assert data['dataout'] != "None" 
        assert resp2.status_code == 200   

    # Test driven development test 
    # Tests whether requesting the default category api using the any invalid
    # entry parameter will return the value "None"
    def test_default_401(self):
        resp2 = None
        entry = "error"
        resp2 = app.test_client().get("/api/" + entry + "/defaultApi")
        data = json.loads(resp2.get_data(as_text=True))  
        assert data['dataout'] == "None" 
        assert resp2.status_code == 401 

if __name__ == "__main__":
    unittest.main()