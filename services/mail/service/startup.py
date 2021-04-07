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
import time 

name = 'mail-service'
description = 'Mail API'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

def get_pubkey():
    for _ in range(20):
        try:
            r = requests.get('http://odonata.keycloak:8080/auth/realms/Odonata')
            break
        except Exception:
            time.sleep(5)

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

def setup(service):
    db = MongoDatabase()
    logic = {'base' : Logic(db,service)}
    return   logic

def connectToBroker(service):

    token = service.get()

    name = 'mail-service'
    pub = 'ticket'
    baseurl= 'http://localhost:5050/pubsub/'
    header = {'Authorization': 'Bearer ' + token}

    res = requests.get(baseurl, headers=header)
    pubs = res.json()['publishers']
    if pub not in [ t['name'] for t in pubs]:
        raise Exception('Messagebroker does not contain the needed Publisher, therefore the corresponding service is not running')

    
    res = requests.get(f'{baseurl}{pub}/{name}', headers=header)

    if  res.status_code == 404:
        data = {'subscriber': 'mail-service', 'callback': 'http://localhost:5025/mail-service/'}
        requests.put(f'{baseurl}ticket', headers=header, data=json.dumps(data))


connectToBroker(service)
logic = setup(service)


