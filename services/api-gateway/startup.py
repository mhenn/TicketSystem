from flask import Flask
from flask_restx import Api 
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import requests
from logic.logic import *
from keycloak_token_service import ServiceToken
from flask_setup import FlaskSetup


setup = FlaskSetup('gateway', __name__)
jwt, api, flask_app, app = setup.get_mandatory()
service = ServiceToken.instance()	
logic = {'base':Logic(service), 'config': ConfigLogic(service)}

