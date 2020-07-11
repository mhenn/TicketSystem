from flask import Flask
from flask_restplus import Api
from db.mongo import MongoDatabase
from logic.logic import Logic

name = 'ticket'
description = 'Ticket API'

flask_app = Flask(__name__)
app = Api(flask_app)
api = app.namespace(name, description=description)


def setupLogic(db):
	return Logic(db)


def setupDB():
	return MongoDatabase()	


def setup():
	db = setupDB()
	logic = setupLogic(db)
	return   logic


logic = setup()
