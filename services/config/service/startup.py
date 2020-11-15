from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from keycloak import KeycloakAdmin
from db.mongo import MongoDatabase
from logic.logic import *



def getAdmin():
    return  KeycloakAdmin(server_url="http://localhost:8000/auth/",
                               username='oadmin',
                               password='oadmin',
                               realm_name="Odonata",
                               verify=True)
#admin = getAdmin()
admin = 0

name = 'config'
description = 'Configuration API'

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

def mongo():
    return MongoClient('mongodb://localhost:27000/')	


jwt = JWTManager(flask_app)
db = MongoDatabase(mongo())

def getLogic(admin, db):
    return {'user': UserLogic(admin), 'queue' : QueueLogic(db), 'mapping': MappingLogic(db), 'mail': MailLogic(db)}

logic = getLogic(admin, db)
