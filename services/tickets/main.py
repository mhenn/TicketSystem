from startup import *
from flask_restplus import  Resource, marshal_with, reqparse
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model, callback_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)

ticket = api.model('Ticket', ticket_model)
callback_msg = api.model('MSG', callback_model)

parser = reqparse.RequestParser()
parser.add_argument('message', location='form')

@api.route("/")
class TicketClass(Resource):
	
	@api.expect(ticket)
	def post(self):
		print(api.payload['body'])
		logic.create(api.payload['body'])
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

	@api.expect(ticket)
	def put(self, ticketID):
		logic.update(api.payload['body'], ticketId)
		return {'status' :200}

@api.route("/callback/")
class Callback(Resource):

	@api.expect(callback_msg)		
	def post(self):
		
		args = parser.parse_args()
		print(args)
		return {'status': 200, 'message':api.payload}
