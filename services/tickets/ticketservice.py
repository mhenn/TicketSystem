from startup import *
from flask_restplus import  Resource, marshal_with
from models.ticket import ticket_model
from logic.logic import *


ticket = api.model('Ticket', ticket_model)


@api.route("/")
@api.expect(ticket)
class TicketClass(Resource):
	
	@api.marshal_with(ticket)
	def post(self):
		logic.update(api.payload)
		return { "status": "Posted new Data"}

	
	@api.marshal_with(ticket)
	def put(self):
		logic.create(api.payload)

@api.route("/<int:ticketID>")
class TicketID(Resource):
	def delete(self, ticketID):
		logic.delete(ticketID)

