from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from db.mongo import MongoDatabase
from logic.logic import *

from logic.token import ServiceToken
import json
import requests

name = 'ticket-service'
description = 'Ticket API'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

def get_pubkey():
    r = requests.get('http://odonata.keycloak:8080/auth/realms/Odonata')
    r = r.json()
    return f"""-----BEGIN PUBLIC KEY-----
{r['public_key']}
-----END PUBLIC KEY-----""" 



flask_app = Flask(__name__)


flask_app.config['JWT_ALGORITHM'] = 'RS256'
flask_app.config['JWT_PUBLIC_KEY'] = get_pubkey()



CORS(flask_app)

app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
api = app.namespace(name, description=description)

jwt = JWTManager(flask_app)

service = ServiceToken()
db = MongoDatabase('mongodb://mongo.ticket:27017/')
url = 'http://odonata.message:5050/pubsub/'

def setup(service, db):
    logic = {'base' : Logic(db), 'pub' : PubLogic(db, service)}
    return   logic

def pubsubAlive():
    res = request.get(url + '/alive/')
    print(res)
    return res.ok

def checkAndCreatePub(service):
    token = service.get() 
    header = {'Authorization': 'Bearer ' + token}
    
    res = requests.get(url, headers=header)
    pubs = res.json()['publishers']
    if 'ticket' not in [ t['publisher'] for t in pubs]:
        data = {'publisher': 'ticket'}
        requests.post(url, headers=header, data=json.dumps(data))
    
try:
    if pubsubAlive: 
        checkAndCreatePub(service)
except Exception as e:
    print(e)
logic = setup(service,db)
