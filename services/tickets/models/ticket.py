from flask_restplus import fields
from api import *

ticket_model = api.model('Ticket',  {
	'id': fields.Integer,
	'subject': fields.String,
	'content': fields.String,
	'appendices': fields.String
})
