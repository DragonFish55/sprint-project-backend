from flask import Flask,json
import unittest
from app import app
from app.models import User, Favorites, db

class FavoritesUnit(unittest.TestCase):
    
    app = Flask(__name__)

    def test_getfavorites_401(self):
        user="user1"
        found = 0
        teststring = "Health"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            User.query.filter_by(username=user).delete()
            Favorites.query.filter_by(username=user).delete()
        resp1 = app.test_client().get('/api/' + user + '/getFavorites')
        data = json.loads(resp1.get_data(as_text=True))

        assert data["dataout"] == "None"
        assert resp1.status_code == 401

    def test_getfavorites_200(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        type_in = "add"
        testdata = {"type":"hey","title":"hey", "author": "there",
                    "pub_date":"127","desc": "this is a test", 
                    "image":"https://hey", "source":"https://there"}

        data_final = "None"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            
            resp2 = app.test_client().post("/api/" + user + "/" + type_in +  "/submitFavorite",
                                    data=json.dumps(testdata),
                                    content_type='application/json')
            
            resp3 = app.test_client().get('/api/' + user + '/getFavorites')
            data_final = json.loads(resp3.get_data(as_text=True))

        assert data_final != "None"

    def test_submitfavorites_add(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        type_in = "add"
        testdata = {"type":"hey","title":"hey", "author": "there",
                    "pub_date":"127","desc": "this is a test", 
                    "image":"https://hey", "source":"https://there"}

        data_final = "None"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            
            resp2 = app.test_client().post("/api/" + user + "/" + type_in +  "/submitFavorite",
                                    data=json.dumps(testdata),
                                    content_type='application/json')
            
            data_final = json.loads(resp2.get_data(as_text=True))

        assert data_final != "None"

    def test_submitfavorites_rem(self):
        user="user1"
        password="pass1"
        resp2 = None
        found = 0
        type_in = "add"
        testdata = {"type":"hey","title":"hey", "author": "there",
                    "pub_date":"127","desc": "this is a test", 
                    "image":"https://hey", "source":"https://there"}

        data_final = "None"
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            find_user = User.query.filter_by(username=user).delete()
        resp1 = app.test_client().post('/api/signup',
                                    data=json.dumps({"username":user,"password":password}),
                                    content_type='application/json')
        
        find_user = User.query.filter_by(username=user).first()
        if(find_user is not None):
            
            resp2 = app.test_client().post("/api/" + user + "/" + type_in +  "/submitFavorite",
                                    data=json.dumps(testdata),
                                    content_type='application/json')
            find_fav = Favorites.query.filter_by(username=user).first()
            if(find_fav is not None):
                type_in = "rem"
                resp3 = app.test_client().post("/api/" + user + "/" + type_in +  "/submitFavorite",
                                    data=json.dumps(testdata),
                                    content_type='application/json')
                data_final = json.loads(resp3.get_data(as_text=True))

        assert data_final != "None"

    def test_submitfavorites_401(self):
        user="user1"
        found = 0
        teststring = "Health"
        type_in = "rem"
        testdata = {"type":"hey","title":"hey", "author": "there",
                    "pub_date":"127","desc": "this is a test", 
                    "image":"https://hey", "source":"https://there"}
        find_user = User.query.filter_by(username=user)
        if(find_user is not None):
            User.query.filter_by(username=user).delete()
            Favorites.query.filter_by(username=user).delete()
        
        resp2 = app.test_client().post("/api/" + user + "/" + type_in +  "/submitFavorite",
                                    data=json.dumps(testdata),
                                    content_type='application/json')
        data1 = json.loads(resp2.get_data(as_text=True))

        assert data1["dataout"] == "None"
        assert resp2.status_code == 401

if __name__ == "__main__":
    unittest.main()