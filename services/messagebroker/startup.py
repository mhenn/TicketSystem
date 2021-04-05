from flask import Flask
#from flask_restplus import Api
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from db.mongo import MongoDatabase
from logic.logic import *


name = 'pubsub'
description = 'Messaging API'

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


db = MongoDatabase()	
base_logic = BaseLogic(db)
publisher_logic = PublisherLogic(db)
pubsub_logic =  PubSubscriberLogic(db)
subscriber_logic = SubscriberLogic(db)

