from flask_restplus import fields
from startup import api

ticket_model = api.model('Ticket',  {
	'id': fields.Integer,
	'subject': fields.String,
	'content': fields.String,
	'appendices': fields.String
})
