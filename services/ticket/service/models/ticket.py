from flask_restx import fields
from startup import api



content_model =  api.model('Content', {
	'timestamp': fields.String,
	'message' : fields.String,
	'appendices': fields.List(fields.Raw)
	
})

ticket_model = api.model('Ticket',  {
        'sender': fields.String,
	'to': fields.String,
	'subject': fields.String,
	'messages': fields.List(fields.Nested(content_model)),
})



update_model = api.model('Ticket',  {
        'id': fields.String,
        'status': fields.String,
        'sender': fields.String,
	'to': fields.String,
	'subject': fields.String,
	'messages': fields.List(fields.Nested(content_model)),
})




callback_model = api.model('MSG', {
	'message': fields.String
})

