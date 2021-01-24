from startup import *
from flask_restx import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model, pub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from decorator import model_integrity
import json
msg = api.model('Message', msg_model)
sub = api.model('Subscription',sub_model)
pub = api.model('Publisher', pub_model)


@api.route("/")
class Base(Resource):
    @jwt_required
    @api.expect(pub)
    @model_integrity(pub_model)
    def post(self):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        try:
            base_logic.create_publisher(json.loads(request.data))
        except:
            return {}, 409
        return {}, 200

    def get(self):
        pubs = base_logic.get_publishers()
        return {'publishers': pubs}, 200	

@api.route("/<string:publisher>")
class Publisher(Resource):

    @jwt_required
    def get(self, publisher):
        pub = publisher_logic.get_publisher(publisher)
        return {'publishers': pub}, 200

    @jwt_required
    @api.expect(msg)
    @model_integrity(msg_model)
    def post(self, publisher):
        publisher_logic.send_msg(publisher, json.loads(request.data))

    @jwt_required
    @api.expect(sub)
    @model_integrity(sub_model)
    def put(self, publisher):
        publisher_logic.add_subscriber(publisher, json.loads(request.data))
        return { 'msg': 'Added subscriber'}, 200	


@api.route("/<string:publisher>/<string:subscriber>")
class PubSubscriber(Resource):

    @jwt_required
    def get(self, publisher, subscriber):
        try:
            sub = pubsub_logic.get_subscriber(publisher,subscriber)
        except ValueError:
            return {}, 404
        return {'publishers': sub}, 200	

    @jwt_required
    def delete(self, publisher, subscriber):
        pubsub_logic.delete_subscriber(publisher, subscriber)
        return {}, 200


