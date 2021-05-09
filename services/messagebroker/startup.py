from flask import Flask
#from flask_restplus import Api
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_setup import FlaskSetup
from db.mongo import MongoDatabase
from logic.logic import *

import requests
import logging


logging.basicConfig(level=logging.DEBUG, filename=f'base.log', format='%(asctime)s %(levelname)s:%(message)s')

setup = FlaskSetup('pubsub', __name__)
jwt, api, flask_app, app = setup.get_mandatory()

db = MongoDatabase()	
base_logic = BaseLogic(db)
publisher_logic = PublisherLogic(db)
pubsub_logic =  PubSubscriberLogic(db)
subscriber_logic = SubscriberLogic(db)

