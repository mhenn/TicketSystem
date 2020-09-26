from startup import *
from flask_restplus import  Resource, marshal_with, reqparse
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model, callback_model
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)


@api.route("/ticket/")
class TicketClass(Resource):
	
	def post(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		logic.post_ticket(request.data)
		return {'status': 200 }

	
	def get(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		logic.get_ticket()
		return {'status': 200 }

