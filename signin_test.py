from flask import jsonify
import flask_unittest
import flask.globals
from app import app
import unittest

class SigninUnit(unittest.TestCase):
    
    app = app

    #check for 200 okay
    def test_ok(client):
            json_obj = {"username":"hey", "password":"there"}
            resp = client.post('/api/signin',json=json_obj)
            assert resp.json == "false"

suite = flask_unittest.LiveTestSuite(app)
suite.addTest(unittest.makeSuite(SigninUnit))

# Run the suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)