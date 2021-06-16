from flask import Flask
from flask_restx import Api 
from flask_jwt_extended import JWTManager
from logic.logic import *
from flask_setup import FlaskSetup
from logic.token import ServiceToken

import logging

logging.basicConfig(level=logging.DEBUG, filename=f'base.log', format='%(asctime)s %(levelname)s:%(message)s')



logging.getLogger('flask_cors').level = logging.DEBUG

service = ServiceToken()
setup = FlaskSetup('gateway', __name__)
jwt, api, flask_app, app = setup.get_mandatory()
logic = {'base':Logic(service), 'config': ConfigLogic(service)}

