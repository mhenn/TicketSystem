from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_oidc import AuthError, JwtManager
#from flask_oidc import OpenIDConnect

from config import Config
from db.mongo import MongoDatabase
from logic.logic import Logic


name = 'ticket'
description = 'Ticket API'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}


flask_app = Flask(__name__)
flask_app.config.update({
    # JWT_OIDC Settings
    'JWT_OIDC_WELL_KNOWN_CONFIG' : 'http://localhost:8000/auth/realms/Odonata/.well-known/openid-configuration',
    'JWT_OIDC_ALGORITHMS' : 'RS256',
    'JWT_OIDC_JWKS_URI' : 'http://localhost:8000/auth/realms/Odonata/protocol/openid-connect/certs' ,
    'JWT_OIDC_ISSUER' : 'http://127.0.0.1:8000/auth/realms/Odonata',
    'JWT_OIDC_AUDIENCE' : 'account',
	 'JWT_OIDC_CLIENT_SECRET' : '39e54d6d-be7e-4820-918a-61b9aa35525e',

    # Flask settings
    'DEBUG' : False,
    'TESTING' : False,
}) 

#oidc = OpenIDConnect(flask_app)

CORS(flask_app)
app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
#app = Api(flask_app)
api = app.namespace(name, description=description)

jwt = JwtManager(flask_app)




def setupLogic(db):
	return Logic(db)

def setupDB():
	return MongoDatabase()	


def setup():
	db = setupDB()
	logic = setupLogic(db)
	return   logic


logic = setup()
