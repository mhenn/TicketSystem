from startup import *
from flask_restx import  Resource
from flask_cors import CORS, cross_origin
from models.ticket import ticket_model, put_ticket_model, callback_model
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from decorator import *
import requests
import json


@api.route("/queues/")
class Queues(Resource):

    @jwt_required
    def get(self):
        queues = logic['base'].get_queues()
        return {'status' : 200, 'queues': queues}

@api.route("/ticket/")
class TicketClass(Resource):

    @jwt_required
    @api.expect(ticket_model)
    @model_integrity(ticket_model)
    def post(self):
        uid = get_jwt_identity()
        print(f'req: {request} data: {json.loads(request.data)} header: {request.headers}')
        id, status = logic['base'].post_ticket(json.loads(request.data), uid)
        return { 'id': id }, status
    @jwt_required
    def get(self):
        uid = get_jwt_identity()
        tickets, status = logic['base'].get_ticket(uid)
        return { "tickets": tickets }, status


@api.route('/ticket/<string:ticketId>/message/<string:messageId>/file/<string:filename>')
class SpecificFile(Resource):
    @jwt_required
    def get(self, ticketId, messageId, filename):
        uid = get_jwt_identity()
        return logic['base'].get_file(ticketId, messageId, filename, uid)

@api.route('/ticket/<string:ticketId>')
class SpecificTicket(Resource):

    @jwt_required
    @model_integrity(put_ticket_model)
    def put(self, ticketId):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        uid = get_jwt_identity()
        status = logic['base'].put_ticket(ticketId, request.data, uid)
        return {}, status 


@api.route('/supporter/ticket/')
class TicketByTopic(Resource):
#TODO change to Get with query params
    @jwt_required
    def post(self):
        response = logic['base'].ticket_topic(request.data)
        return response, 200
	
@api.route('/ticket/<string:ticketId>/message/<string:messageId>/files/')
class SpecificTicket(Resource):

    @jwt_required
    def post(self, ticketId, messageId):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        files = request.files.to_dict()	
        uid = get_jwt_identity()
        status = logic['base'].post_files(ticketId, uid, messageId, files)	
        return {'status': status}

@api.route('/config/role-mapping/')
class RoleMapping(Resource):

    @jwt_required
    def get(self):
        mapping, status = logic['config'].get_mapping()
        return mapping, status
