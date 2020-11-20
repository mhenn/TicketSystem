from flask_restx import fields
from startup import api

sub_model = api.model('Subscription',  {
	'subscriber': fields.String,
	'callback': fields.String
})

msg_model = api.model('Message', {
	'message' : fields.String
})


pub_model = api.model('Publisher', {
	'publisher' : fields.String
})
