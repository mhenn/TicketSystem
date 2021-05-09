from flask import Flask
from flask_restx import Api 
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from logic.logic import *
from flask_setup import FlaskSetup
from logic.token import ServiceToken

import logging


logging.basicConfig(level=logging.DEBUG, filename=f'base.log', format='%(asctime)s %(levelname)s:%(message)s')

service = ServiceToken()
setup = FlaskSetup('gateway', __name__)
jwt, api, flask_app, app = setup.get_mandatory()
logic = {'base':Logic(service), 'config': ConfigLogic(service)}

