from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_oidc import AuthError, JwtManager

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
flask_app.config.update(TEST=True)
CORS(flask_app)
app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
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
