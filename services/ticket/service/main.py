from startup import *
from flask_restplus import  Resource, marshal_with, reqparse
from flask_cors import CORS, cross_origin
from models.ticket import  content_model, ticket_model, callback_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import requests

parser = reqparse.RequestParser()
parser.add_argument('message', location='form')

@api.route("/")
class TicketClass(Resource):

	@jwt_required	
	@api.expect(ticket_model)
	def post(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		logic.create(request.data)
		return {'status': 200 }

	@jwt_required
	def get(self):
		tickets = logic.get()
		return {'status': 200, 'tickets': tickets}

@api.route("/<string:ticketID>")
class TicketID(Resource):
	@jwt_required
	def delete(self, ticketID):
		logic.delete(ticketID)
		return {'status':200}

	@api.expect(ticket_model)
	def put(self, ticketID):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		logic.update(request.data, ticketID)
		return {'status' :200}

@api.route("/callback/")
class Callback(Resource):

	@api.expect(callback_model)		
	def post(self):
		
		args = parser.parse_args()
		return {'status': 200, 'message':api.payload}


@api.route('/unused')
class Placeholder(Resource):
	@jwt_required
	@api.expect(content_model)
	def get(self):
		return {'status': 404, 'message': "How about NO!!!"}


