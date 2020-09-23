from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)

msg = api.model('Message', msg_model)
sub = api.model('Subscription',sub_model)


@api.route("/")
class TicketClass(Resource):
	
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

	def put(self, ticketID):
		logic.update(api.payload['body'], ticketId)
		return {'status' :200}


