from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model, pub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import json
msg = api.model('Message', msg_model)
sub = api.model('Subscription',sub_model)
pub = api.model('Publisher', pub_model)

@api.route("/")
class Base(Resource):
    @jwt_required
    @api.expect(pub)
    def post(self):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        base_logic.create_publisher(json.loads(request.data))
        return {'status': 200 }

    @jwt_required
    def get(self):
        pubs = base_logic.get_publishers()
        return {'status': 200, 'publishers': pubs}	

@api.route("/<string:publisher>")
class Publisher(Resource):

    @jwt_required
    def get(self, publisher):
        pub = publisher_logic.get_publisher(publisher) 
        return {'status': 200, 'publisher': pub}	

    @jwt_required
    @api.expect(msg)
    def post(self, publisher):
        publisher_logic.send_msg(publisher, json.loads(request.data))

    @jwt_required
    @api.expect(sub)	
    def put(self, publisher):
        publisher_logic.add_subscriber(publisher, json.loads(request.data))
        return {'status': 200, 'msg': 'Added subscriber'}	


    @jwt_required
    def delete(self, publisher):
        pass


@api.route("/<string:publisher>/<string:subscriber>")
class PubSubscriber(Resource):

    @jwt_required
    def get(self, publisher, subscriber):
        try:
            sub = pubsub_logic.get_subscriber(publisher,subscriber)
        except ValueError:
            return {'message': 404}, 404
        return {'status': 200, 'publishers': sub}	

    @jwt_required
    def delete(self, publisher, subscriber):
        pubsub_logic.delete_subscriber(publisher, subscriber)
        return {'status': 200}


class Subscriber(Resource):

    @jwt_required
    def get(self, subscriber):
        pass
        return {'status': 200, 'publishers': pubs}	

    @jwt_required
    def delete(self, subscriber):
        pass
