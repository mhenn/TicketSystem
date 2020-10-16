from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model, pub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import json

@api.route("/queues/")
class Queue(Resource):

    def post(self):
        queue = json.loads(request.data)
        logic['queue'].create(queue)
        return {'status': 200 }

    def get(self):
        print(logic)
        queues = logic['queue'].get()
        return {'status': 200, 'queues': queues}	


@api.route("/queues/<string:queueId>")
class SpecificQueue(Resource):

    def delete(self, queueId):
        status =  logic['queue'].delete(queueId)
        return {'status': status}


@api.route("/roles/")
class Roles(Resource):

    def post(self):
        pass

    def get(self):
        pass
