from flask_restx import fields
from startup import api


queue_model = api.model('Queue', {
    'title': fields.String(required=True)
})

mail_model = api.model('Mail', {
    'title': fields.String
})
