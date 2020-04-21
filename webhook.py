import json #to convert list and dictionary to json
import os
import requests
from flask import Flask #it is microframework to develop a web app from flask import request
from flask import make_response
#Falsk app for our web app
app=Flask(__name__)
# app route decorator. when webhook is called, the decorator would call the functions which are e defined
@app.route('/webhook', methods=['POST'])
def webhook():
    req=request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4)) #extract the relevant information and use api and get the response and send it dialogflow. #helper function
    res=makeResponse(req)
    res=json.dumps(res, indent=4)
    r=make_response(res)
    r.headers['Content-Type']='application/json'
    return r
# extract parameter values, query weahter api, construct the resposne
def makeResponse(req):
    result=req.get("queryResult")