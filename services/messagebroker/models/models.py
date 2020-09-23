from flask_restplus import fields
from startup import api

sub_model = api.model('Subscription',  {
	'publisher': fields.String,
	'subscriber': fields.String,
})

msg_model = api.model('Message', {
	'publisher': fields.String,
	'message' : fields.String
})
