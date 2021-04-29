from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from config import Config
from db.mongo import MongoDatabase
from logic.logic import *

from keycloak_token_service import ServiceToken
from logic.token import ServiceToken
import json
import requests
import time
import logging


from keycloak_token_service import ServiceToken
setup = FlaskSetup('ticket-service', __name__)
jwt, api, flask_app, app = setup.get_mandatory()

logging.basicConfig(level=logging.DEBUG, filename=f'{name}.log', format='%(asctime)s %(levelname)s:%(message)s')

service = ServiceToken()
db = MongoDatabase('mongodb://mongo.ticket:27017/')
url = 'http://odonata.message:5050/pubsub/'

def setup(service, db):
    logic = {'base' : Logic(db), 'pub' : PubLogic(db, service)}
    return   logic

def pubsubAlive():
    res = request.get(url + '/alive/')
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
    logging.error(e)
logic = setup(service,db)
