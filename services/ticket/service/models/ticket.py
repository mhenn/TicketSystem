from flask_restplus import fields
from startup import api




content_model =  api.model('Content', {
	'timestamp': fields.DateTime(),
	'message' : fields.String,
	'appendices': fields.List(fields.Raw)
	
})

ticket_model = api.model('Ticket',  {
	'id': fields.Integer,
	'from': fields.String,
	'to': fields.String,
	'subject': fields.String,
	'messages': fields.List(fields.Nested(content_model)),
	'status': fields.String
})

callback_model = api.model('MSG', {
	'message': fields.String
})

