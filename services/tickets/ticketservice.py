from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model
from logic.logic import *


ticket = api.model('Ticket', ticket_model)


@api.route("/")
class TicketClass(Resource):
	
	@api.marshal_with(ticket)
	@api.expect(ticket)
	def post(self):
		logic.update(api.payload)
		return { "status": "Posted new Data"}

	
	@api.marshal_with(ticket)
	@api.expect(ticket)
	def put(self):
		logic.create(api.payload)
		return {"status": "Put stuff"}

	def get(self):
		tickets = logic.get()
		print(tickets)
		return {"status": 200, "tickets": tickets}

@api.route("/<int:ticketID>")
class TicketID(Resource):
	def delete(self, ticketID):
		logic.delete(ticketID)

