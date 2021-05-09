from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from db.mongo import MongoDatabase
from logic.logic import *

import json
import requests
import time 
from keycloak_token_service import ServiceToken
from flask_setup import FlaskSetup


setup = FlaskSetup('gateway', __name__)
jwt, api, flask_app, app = setup.get_mandatory()
service = ServiceToken.instance()

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


