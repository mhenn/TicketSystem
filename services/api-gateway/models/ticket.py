from flask_restx import fields
from startup import api

ticket_model = api.model('Ticket',  {
	'sender': fields.String(required=True),

	'to': fields.String(required=True),
	'subject': fields.String(required=True),
	'messages': fields.String(required=True),
})

put_ticket_model = api.model('PUT_TICKET',{
    'ticket': fields.Nested(ticket_model)
    })

callback_model = api.model('MSG', {
	'message': fields.String
})

