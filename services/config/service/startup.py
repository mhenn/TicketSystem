from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from keycloak import KeycloakAdmin
from db.mongo import MongoDatabase
from logic.logic import *
import requests 
import time



def getAdmin():
    return  KeycloakAdmin(server_url="http://odonata.keycloak:8080/auth/",
                               username='oadmin',
                               password='oadmin',
                               realm_name="Odonata",
                               verify=True)



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
flask_app.config['JWT_PUBLIC_KEY'] = get_pubkey() 



CORS(flask_app)

app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
api = app.namespace(name, description=description)



jwt = JWTManager(flask_app)

db = MongoDatabase('mongodb://mongo.config:27017/')

def getLogic(admin, db):
    return {'user': UserLogic(admin), 'queue' : QueueLogic(db), 'mapping': MappingLogic(db), 'mail': MailLogic(db)}

logic = getLogic(admin, db)
