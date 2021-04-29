from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from keycloak import KeycloakAdmin
from db.mongo import MongoDatabase
from logic.logic import *
import requests 
import time
from keycloak_token_service import ServiceToken
setup = FlaskSetup('configuration-service', __name__)
jwt, api, flask_app, app = setup.get_mandatory()




def getAdmin():
    return  KeycloakAdmin(server_url="http://odonata.keycloak:8080/auth/",
                               username='oadmin',
                               password='oadmin',
                               realm_name="Odonata",
                               verify=True)


#admin = getAdmin()
admin = 0
db = MongoDatabase('mongodb://mongo.config:27017/')

def getLogic(admin, db):
    return {'user': UserLogic(admin), 'queue' : QueueLogic(db), 'mapping': MappingLogic(db), 'mail': MailLogic(db)}

logic = getLogic(admin, db)
