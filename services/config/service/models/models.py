from flask_restx import fields
from startup import api


queue_model = api.model('Queue', {
    'title': fields.String(required=True)
})

mail_model = api.model('Mail', {
    
    "name": fields.String(required=True),
    "mappingId": fields.String(required=True) ,
    "type": fields.String(required=True),
    "actions":fields.List(fields.String, required=True)
})

role_model = api.model('Role', {
    
    "name": fields.String(required=True),
    "id": fields.String(required=True) ,
    "children":fields.List(fields.String, required=True)
})
