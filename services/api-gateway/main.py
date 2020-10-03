from startup import *
from flask_restplus import  Resource, marshal_with, reqparse
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model, callback_model
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import json

@api.route("/ticket/")
class TicketClass(Resource):

	@jwt_required
	def post(self):
		uid = get_jwt_identity()
		print(f'req: {request} data: {json.loads(request.data)} header: {request.headers}')
		status, id = logic.post_ticket(json.loads(request.data))
		return {'status': status, 'id': id }

	@jwt_required
	def get(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		tickets = logic.get_ticket()
		return {'status': 200, "tickets": tickets }


@api.route("/ticket/files")
class TicketFiles(Resource):

	@jwt_required
	def post(self):
		pass

@api.route('/ticket/<string:ticketId>')
class SpecificTicket(Resource):

	@jwt_required
	def put(self, ticketId):
		print("PUT")	
		print(f'req: {request} data: {request.data} header: {request.headers}')
		status = logic.put_ticket(ticketId, request.data)
		return {'status': status}
