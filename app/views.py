import datetime
from app import app
from flask import make_response, request,jsonify, session
from flask_cors import cross_origin
from .models import db, User
from cryptography.fernet import Fernet
from app import usersettings
import requests



#defines the signup api endpoint
@app.route('/api/signup', methods = ["POST"])
@cross_origin(supports_credentials=True)
def signup():
    #get incoming json data
    response_code = 200
    data_out = 'false'
    data_in = request.get_json()
    user = data_in["username"]
    password = data_in['password']
    #if username is in database generate encrypted key and
    #create new user otherwise signup failed and output 401
    find_user = User.query.filter_by(username=user).first()
    if(find_user is None):
        enc_key = Fernet.generate_key()
        enc_key_dec = enc_key.decode()
        fernet_var = Fernet(enc_key)
        encrypted_pass = fernet_var.encrypt(password.encode())
        firstpass = encrypted_pass.decode()
        new_user = User(username=user,password=firstpass,enc_key=enc_key_dec,usertypes="")
        db.session.add(new_user)
        db.session.commit()
        data_out = "true"    
    else:
        response_code = 401

    return jsonify({'data_out':data_out}),response_code

#defines the signin api endpoint
@app.route('/api/signin', methods = ["POST"])
@cross_origin(supports_credentials=True)
def signin():
    response_code = 200
    user_err = "false"
    pass_err = "false"
    encrypt_pass = ""
    data_in = request.get_json()
    user = data_in['username']
    password = data_in['password']
    #if user is in database table decrypt the table password
    #and if the passwords match return 200 ok otherwise return 401
    find_user = User.query.filter_by(username=user).first()
    print(find_user)
    if(find_user is not None):
       
        #app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
        print(session)
        user_err = "false"
        #session["username"] = user
        enc_key = find_user.enc_key
        enc_key = enc_key.encode()
        fernet_var = Fernet(enc_key)
        saved_pass = find_user.password
        encrypt_pass = fernet_var.decrypt(saved_pass.encode()).decode()
        if(password == encrypt_pass):
            pass_err = "false"
            response_code = 200
        else:
            pass_err = "true"
            response_code = 401  
    else:
        user_err = "true"
        pass_err = "true"
        response_code = 401
    
    resp_def = make_response((jsonify({'user_error':user_err, "pass_error":pass_err}),response_code))
    resp_def.set_cookie("username", value=user, domain="127.0.0.1",samesite='None', secure=True, \
                                                                                    expires=datetime.datetime.now() \
                                                                                            + datetime.timedelta(days=30))
    #resp_def.headers.add('Set-Cookie','cross-site-cookie=username; SameSite=None; Secure')
    print(resp_def)
   
    return resp_def
    
    #data_out.headers.add('Access-Control-Allow-Origin', '*')
    #data_out.headers.add('Access-Control-Allow-Headers', '*')

@app.route('/api/<user>/getApiData', methods = ["GET"])
@cross_origin(supports_credentials=True)
def getsession(user="defuser"):
    response_code = 200
    data_out = None
    data = None
    json_data = []
    #name = session['username']
    print(user)
    find_user = User.query.filter_by(username=user).first()
    print(find_user)
    if(find_user != None):
        if(find_user.user_types != ""):
            usersettings.articles_types = find_user.user_types.split(',')
            for i in usersettings.articles_types:
                data = callApi(i)
                data = [i,data]
                json_data.append(data)
                
        else:
            response_code = 200
            json_data = "None"
    else:
        response_code = 401
        data = None
    return jsonify({"dataout":json_data}), response_code

@app.route('/api/<entry>/defaultApi', methods = ["GET"])
@cross_origin(supports_credentials=True)
def getDefaultApi(entry="top_headline"):
    response_code = 200
    json_data = []
    n = request.query_string.decode()
    print(n)
    if(entry == "top_headline"):
        data = callApi("General")
        data = ["General",data]
    elif(entry == "everything"):
        data = callEvery(entry)
    json_data.append(data)
    return jsonify({"dataout":json_data}), response_code

#signout api
@app.route('/api/signout', methods = ["POST"])
@cross_origin(supports_credentials=True)
def signout():
    
    response_code = 200
    data_out = "false"
    data_in = request.get_json()
    user = data_in['username']
    print(user)
    #if user in table then respond 200 otherwise respond 404
    #also signal user to logout if ok
    find_user = User.query.filter_by(username=user).first()
    print(find_user)
    if(find_user is not None):
        data_out = "true"
        response_code = 200
    else:
        response_code = 404

    resp_def = make_response((jsonify({'user_error':data_out}),response_code))
    resp_def.set_cookie("username", value='', samesite='None', domain="127.0.0.1",secure=True, expires=0)
    
    return resp_def

#defines the settings api endpoint for submitting the categories
#to the database
@app.route('/api/new/<user>/categories', methods = ["GET"])
@cross_origin(supports_credentials=True)
def getcategory(user="defuser", category="General"):
    newstring = ""
    data_out = "true"
    typechk = None
    response_code = 200
    cat_data =[]
    i = 0
    param_val = ""
    p = []
    n = request.query_string.decode()
    username = user
    print(username)
    #removes timestamp and then splits entries into list
    l = n.split("&_=")[0].split("&")
    print(l)
    find_user = User.query.filter_by(username=user).first()
    print(find_user)
    if(find_user != None):
        if(find_user.user_types != ""):
            typechk = find_user.user_types.split(',')
        else:
            typechk = [""]
        for i in l:
            param_val = i.split("=")
            
            if(param_val[1].lower() == "true"):
                if(not(param_val[0] in typechk)):
                    if(find_user.user_types == ""):
                        find_user.user_types = param_val[0]
                    else:
                        find_user.user_types = find_user.user_types + "," + param_val[0]
                    db.session.commit()
            else:
                if(param_val[0] in typechk):
                    find_type = find_user.user_types.find(param_val[0].lower())
                    typelen = len(param_val[0])
                    if(find_type + typelen == len(find_user.user_types)):
                        if(find_type == 0):
                            newstring = None
                        else:
                            newstring = find_user.user_types[0:find_type-1]
                        #print(find_user.user_types[0:find_type-1])
                        #print("i: " + str(i))
                        #print(newstring)
                        #print("only one")
                        #print("---------------")
                        
                    else:
                        if(find_type == 0):
                            if(',' in find_user.user_types):
                                newstring = find_user.user_types[(typelen+1):len(find_user.user_types)]
                                if(newstring == ""):
                                    newstring = None
                            else:
                                newstring = None
                            #print(find_user.user_types[typelen:len(find_user.user_types)-1])
                            #print("i: " + str(i))
                            #print(newstring)
                            #print("at beginning")
                            #print("---------------")
                            
                        else:
                            newstring = find_user.user_types[0:find_type-1] + "," + \
                                    find_user.user_types[(find_type+1 + typelen):len(find_user.user_types)]
                            if(newstring == ""):
                                    newstring = None
                            #print(find_user.user_types[0:find_type-1])
                            #print(find_user.user_types[(find_type+1 + typelen):len(find_user.user_types)])
                            #print("i: " + str(i))
                            #print(newstring)
                            #print("in middle")
                            #print("---------------")
                        #print("i" + str(i))
                        #print("Beginning" + str(find_user.user_types[0:find_type-1]))
                        #print("End" + find_user.user_types[(find_type + 1 + typelen):len(find_user.user_types)])
                        
                        
                    find_user.user_types = newstring
                    
                    db.session.commit()

        usersettings.articles_types = find_user.user_types.split(',')
        print(usersettings.articles_types)
    else:
        data_out = "false"
        response_code = 401

    print(response_code)

    return jsonify({"dataout":data_out}), response_code

'''
#defines the endpoint for retrieving the api data
#and sending back to the frontend
@app.route('/api/<user>/settings', methods = ["POST"])
@cross_origin()
def setSettings():
    response_code = 200
    data_out = 'false'
    data_in = request.get_json()
    cat_data[i] = callApi(param_val[0])
    i = i+1
    for k in range(0,l,1):
        p[k] = {param_val:cat_data[k]}
    return jsonify({"hi":"there"})
'''

#function that updates the current category that you want to view
def setCategory(category):
    if(category == "Business"):
        usersettings.articles_curr = "Business"
    elif(category == "Entertainment"):
        usersettings.articles_curr = "Entertainment"
    elif(category == "Health"):
        usersettings.articles_curr = "Health"
    elif(category == "Science"):
        usersettings.articles_curr = "Science"
    elif(category == "Sports"):
        usersettings.articles_curr = "Sports"
    elif(category == "Technology"):
        usersettings.articles_curr = "Technology"
    else:
        usersettings.articles_curr = "General"


#function that call the api and returns the data for
#the given category
def callApi(category):
    api_key = usersettings.api_key
    query = {"category":category,"apiKey":api_key, "language":"en", "pageSize":10}
    req = requests.get('https://newsapi.org/v2/top-headlines', 
                        params=query)

    return req.json()
    #api_key = usersettings.api_key
    #query = {"category":category,"apiKey":api_key, "country":"us"}
    #req = requests.get('https://newsapi.org/v2/top-headlines/sources', 
    #                    params=query)
    #print(req)

def callEvery(entry):
    api_key = usersettings.api_key
    query = {"sortBy": "relevancy","language":"en","q":entry,"apiKey":api_key, "language":"en"}
    req = requests.get('https://newsapi.org/v2/everything', 
                        params=query)
    return req.json()

#create app tables
with app.app_context():
    db.create_all()