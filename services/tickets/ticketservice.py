from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model
from logic.logic import *
from flask_jwt_extended import (jwt_required, get_jwt_identity)

ticket = api.model('Ticket', ticket_model)


@api.route("/")
class TicketClass(Resource):
	
	@cross_origin(origin='/*')
	@api.expect(ticket)
	def post(self):
		logic.create(api.payload)
		return {'status', 200 }

	
	@cross_origin(origin='*')
	@api.expect(ticket)
	def put(self):
		logic.update(api.payload)
		return {'status' :200}

	@jwt_required
	def get(self):
		tickets = logic.get()
		print(tickets)
		return {'status': 200, 'tickets': tickets}

@api.route("/<string:ticketID>")
class TicketID(Resource):
	@jwt_required
	@cross_origin(origin='*')
	def delete(self, ticketID):
		logic.delete(ticketID)
		return {'status':200}


