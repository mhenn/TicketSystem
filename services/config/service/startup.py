from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from keycloak import KeycloakAdmin
from db.mongo import MongoDatabase
from logic.logic import *
from keycloak_token_service import ServiceToken
from flask_setup import FlaskSetup
import requests 
import time
import logging

logging.basicConfig(level=logging.DEBUG, filename=f'base.log', format='%(asctime)s %(levelname)s:%(message)s')
setup = FlaskSetup('config', __name__)
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
