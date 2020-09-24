from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model, pub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)

msg = api.model('Message', msg_model)
sub = api.model('Subscription',sub_model)
pub = api.model('Publisher', pub_model)

@api.route("/")
class Base(Resource):
	
	@api.expect(pub)
	def post(self):
		base_logic.create_publisher(api.payload['publisher'])
		return {'status': 200 }

	def get(self):
		pubs = base_logic.get_publishers()
		return {'status': 200, 'publishers': pubs}	

@api.route("/<string:publisher>")
class Publisher(Resource):
	
	def get(self, publisher):
		pub = publisher_logic.get_publisher(publisher) 
		return {'status': 200, 'publisher': pub}	

	@api.expect(msg)
	def post(self, publisher):
		publisher_logic.send_msg(publisher, api.payload['message'])

	@api.expect(sub)	
	def put(self, publisher):
		publisher_logic.add_subscriber(publisher, api.payload)
		return {'status': 200, 'msg': 'Added subscriber'}	

		
	def delete(self, publisher):
		pass


@api.route("/<string:publisher>/<string:subscriber>")
class PubSubscriber(Resource):

	def get(self, publisher, subscriber):
		try:
			sub = pubsub_logic.get_subscriber(publisher,subscriber)
		except ValueError:
			return {'status': 404}
		return {'status': 200, 'publishers': sub}	

	def delete(self, publisher, subscriber):
		pubsub_logic.delete_subscriber(publisher, subscriber)
		return {'status': 200}


class Subscriber(Resource):
	
	def get(self, subscriber):
		pass
		return {'status': 200, 'publishers': pubs}	
	
	def delete(self, subscriber):
		pass
