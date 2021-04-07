from startup import *
from flask_restx import  Resource, marshal
from flask_cors import CORS, cross_origin
from models.models import queue_model, mail_model, role_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import json
from decorator import model_integrity

def normalize_query_param(value):
    return value if len(value) > 1 else value[0]

def normalize_query(params):
    params_non_flat = params.to_dict(flat=False)
    return {k: normalize_query_param(v) for k,v in params_non_flat.items()}


@api.route("/mail/")
class User(Resource):


    def get(self):
        query = normalize_query(request.args)
        print(query)
        return logic['user'].get_by_roles(query['data'])


@api.route("/queues/")
class Queue(Resource):
   
    @jwt_required()
    @model_integrity(queue_model)
    def post(self):
        queue = json.loads(request.data)
        logic['queue'].create(queue)
        return {}, 200

    @jwt_required()
    def get(self):
        queues = logic['queue'].get()
        return {'status': 200, 'queues': queues}	


@api.route("/queues/<string:queueId>")
class SpecificQueue(Resource):

    def delete(self, queueId):
        status =  logic['queue'].delete(queueId)
        return {'status': status}, 200


@api.route("/mail-mapping/<string:mailMappingId>")
class Mail(Resource):

    @jwt_required()
    def delete(self, mailMappingId):
        logic['mail'].delete(mailMappingId)
        return


@api.route("/mail-mapping/")
class Mail(Resource):
    
    @jwt_required()
    @model_integrity(mail_model)
    def post(self):
        mapping = json.loads(request.data)
        logic['mail'].create(mapping)
        return

    @jwt_required()
    def get(self):
        mapping = logic['mail'].get()
        return { "mapping": mapping}


@api.route("/role-mapping/")
class Mappings(Resource):

    @jwt_required()
    @model_integrity(role_model)
    def post(self):
        mapping = json.loads(request.data)
        logic['mapping'].create(mapping)
        return {'status': 200 }

    @jwt_required()
    def get(self):
        mapping = logic['mapping'].get()
        return {'status': 200, 'mapping': mapping}


@api.route('/role-mapping/<string:mappingId>')
class SpecificMapping(Resource):


    def delete(self, mappingId):
        status = logic['mapping'].delete(mappingId)
        return {'status': status}
