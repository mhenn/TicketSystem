from flask_restx import fields
from startup import api

ticket_model = api.model('Ticket',  {
    'id': fields.Integer(required=True),
	'sender': fields.String(required=True),

	'to': fields.String(required=True),
	'subject': fields.String(required=True),
	'messages': fields.String(required=True),
	'status': fields.String
})

put_ticket_model = api.model('PUT_TICKET',{
    'ticket': fields.Nested(ticket_model)
    })

callback_model = api.model('MSG', {
	'message': fields.String
})

