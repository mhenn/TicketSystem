from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_oidc import AuthError, JwtManager
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


flask_app = Flask(__name__)


flask_app.config['JWT_ALGORITHM'] = 'RS256'
flask_app.config['JWT_IDENTITY_CLAIM'] = 'sub'
flask_app.config['JWT_PUBLIC_KEY'] =  """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAslHDNkPEF4Xmjz8yd16l
UG15Bhr2YLkh8v6D9OCEvCNRsDq2JFqbAcxCfRnXIKjs/7n2Dv6jaU0X8FP6noEf
GHPyhlLJb/mIk/rTSEatZy0Mf/cbBkF90sJX5dilh/yCn5ygICqJ0egyQJhnrF7w
lp4JnJ2sCXySUaPmX0DyJPfhPuDMT17HktGD+F8e5SbDK8yGeoxqfkdhw5GnSzvI
poCMoSX4h8JUWUevZvKikFI377uuBDkjsuI4D6Mj5BKU7Up6cW/fsKHAWt71s1c0
B2U9tf7FIlN4r5xXSRlk0IKZ9NIvEAr3k3JIFrZQeThu9ITM66Rne9Ndh1HoIOEY
6QIDAQAB
-----END PUBLIC KEY-----"""

flask_app.config['JWT_DECODE_AUDIENCE'] = 'account'



CORS(flask_app)

app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
api = app.namespace(name, description=description)

jwt = JWTManager(flask_app)

service = ServiceToken()
db = MongoDatabase('mongodb://localhost:27017/')
url = 'http://localhost:5050/pubsub/'

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
    if 'ticket' not in [ t['name'] for t in pubs]:
        data = {'publisher': 'ticket'}
        requests.post(url, headers=header, data=json.dumps(data))
    
try:
    if pubsubAlive: 
        checkAndCreatePub(service)
except Exception as e:
    print(e)
logic = setup(service,db)
