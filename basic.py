from flask import Flask
from flask_restplus import Api, Resource, fields, marshal_with


flask_app = Flask(__name__)
app = Api(app = flask_app)

api = app.namespace('ticket', description='Ticket API')

ticket = api.model('Ticket', {
	'id' : fields.Integer,
	'subject' : fields.String,
	'content' : fields.String,
	'appendices' : fields.String
}) 

@api.route("/")
@api.expect(ticket)
class TicketClass(Resource):
	
	@api.doc(model='Ticket')
	def post(self):
		print(api.payload)
		return { "status": "Posted new Data"}


