from flask_restx import fields
from startup import api

ticket_model = api.model('Ticket',  {
	'id': fields.Integer,
	'from': fields.String,
	'to': fields.String,
	'subject': fields.String,
	'content': fields.String,
	'appendices': fields.String,
	'status': fields.String
})

callback_model = api.model('MSG', {
	'message': fields.String
})

