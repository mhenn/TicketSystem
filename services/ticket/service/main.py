from startup import * 
from flask_restx import Resource
from flask_cors import CORS, cross_origin
from models.ticket import  content_model, ticket_model, callback_model
from logic.logic import *
from flask import request, send_from_directory
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import requests
import json
import os

@api.route('/ticket/<string:ticketId>/message/<string:messageId>')
class UserFileUpload(Resource):
    @jwt_required
    def post(self,  ticketId, messageId):
        print(f'req: {request} form: {request.form.to_dict()} files: {request.files.to_dict()} header: {request.headers}')
        files = request.files.to_dict()
        form = request.form.to_dict()
        print( logic['base'].createFiles(files, form['uid'], ticketId, messageId))
        return {'status':200}

@api.route('/ticket/topics/')
class TicketByTopics(Resource):

    @jwt_required
    def post(self):
        tickets = logic['base'].getTicketByTopic(json.loads(request.data))
        return {'tickets': tickets}

@api.route('/ticket/<string:ticketId>')
class TicketById(Resource):

    @jwt_required
    def get(self, ticketId):
        ticket = logic['base'].get_by_id(ticketId)

        return {'ticket': ticket}


@api.route('/user/<string:uid>/ticket/<string:ticketId>/message/<string:messageId>/file/<string:filename>')
class FileDownload(Resource):
    @jwt_required
    def get(self, ticketId, uid, messageId, filename):
        return send_from_directory(f'./files/{uid}/{ticketId}/{messageId}', filename, as_attachment=True)


@api.route("/user/<string:userId>")
class TicketClass(Resource):

    @jwt_required	
    @api.expect(ticket_model)
    def post(self, userId):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        id = logic['base'].create(json.loads(request.data), userId)

        logic['pub'].created(str(id))

        return { 'id': str(id)}, 200

    @jwt_required
    def get(self, userId):
        tickets = logic['base'].get_by_uid(userId)
        print(len(tickets))
        return {'status': 200, 'tickets': tickets}


@api.route("/user/<string:userId>/ticket/<string:ticketID>")
class TicketID(Resource):

    @jwt_required
    def delete(self, userId, ticketID):
        logic['base'].delete(ticketID)
        return {'status':200}

    @api.expect(ticket_model)
    def put(self, userId, ticketID):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        logic['base'].update(request.data, ticketID)
        logic['pub'].updated(ticketID)
        return {'status' :200}

@api.route("/callback/")
class Callback(Resource):

    @api.expect(callback_model)		
    def post(self):
        return {'status': 200}


@api.route('/unused')
class Placeholder(Resource):
    @jwt_required
    @api.expect(content_model)
    def get(self):
        return {'status': 404, 'message': "How about NO!!!"}


