from api import *
from flask_restplus import  Resource, marshal_with
from models.ticket import ticket_model
from logic import *


ticket = api.model('Ticket', ticket_model)

@api.route("/")
@api.expect(ticket)
class TicketClass(Resource):
	
	@api.marshal_with(ticket)
	def post(self):
		return { "status": "Posted new Data"}

	
	@api.marshal_with(ticket)
	def put(self):
		create(api.payload)
		pass

	@api.marshal_with(ticket)
	def delete(self):
		pass

