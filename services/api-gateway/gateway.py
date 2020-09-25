from startup import *
from flask_restplus import  Resource, marshal_with, reqparse
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model, callback_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)

parser = reqparse.RequestParser()
parser.add_argument('message', location='form')

@api.route("/ticket/")
class TicketClass(Resource):
	
	def post(self):
		return {'status': 200 }

	
	def get(self):
		return {'status': 200 }

