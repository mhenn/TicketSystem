from startup import * 
from flask_restx import Resource
from flask_cors import CORS, cross_origin
from models.ticket import  content_model, ticket_model, callback_model, update_model
from logic.logic import *
from flask import request, send_from_directory
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from decorator import *
import threading
import requests
import json
import os

#TODO Needs overhaul, file upload shouldnt need a uid and just the messageObj should be send as update
@api.route('/ticket/<string:ticketId>/message/<string:messageId>')
class UserFileUpload(Resource):
    @jwt_required()
    def post(self,  ticketId, messageId):
        print(f'req: {request} form: {request.form.to_dict()} files: {request.files.to_dict()} header: {request.headers}')
        files = request.files.to_dict()
        form = request.form.to_dict()    
        logic['base'].createFiles(files, form['uid'], ticketId, messageId)
        return {'status':200}

@api.route('/ticket/topics/')
class TicketByTopics(Resource):

    @jwt_required()
    def post(self):
        tickets = logic['base'].getTicketByTopic(json.loads(request.data))
        return {'tickets': tickets}


@api.route('/ticket/<string:ticketId>')
class TicketById(Resource):

    @jwt_required()
    def get(self, ticketId):
        ticket, status = logic['base'].get_by_id(ticketId)
        return {'ticket': ticket}, status

    #TODO also send file.  
    @jwt_required()
    @model_integrity(content_model)
    @api.expect(content_model) 
    def put(self, ticketId):
        status = logic['base'].appendMessage(ticketId, json.loads(request.data))
        return {}, status


@api.route('/user/<string:uid>/ticket/<string:ticketId>/message/<string:messageId>/file/<string:filename>')
class FileDownload(Resource):
    @jwt_required()
    def get(self, ticketId, uid, messageId, filename):
        try:
            return  send_from_directory(f'./files/{uid}/{ticketId}/{messageId}', filename, as_attachment=True)
        except Exception as e:
            return {}, 500

@api.route("/user/<string:userId>")
class TicketClass(Resource):

    @jwt_required()	
    @model_integrity(ticket_model)
    @api.expect(ticket_model)
    def post(self, userId):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        id = logic['base'].create(json.loads(request.data), userId)

        #logic['pub'].created(str(id))
        x = threading.Thread(target=logic['pub'].updated, args=(str(id),))
        x.start()

        return { 'id': str(id)}, 200

    @jwt_required()
    def get(self, userId):
        tickets = logic['base'].get_by_uid(userId)
        print(len(tickets))
        return {'status': 200, 'tickets': tickets}


@api.route("/user/<string:userId>/ticket/<string:ticketID>")
class TicketID(Resource):

    @jwt_required()
    def delete(self, userId, ticketID):
        logic['base'].delete(ticketID)
        return {'status':200}

    @model_integrity(update_model)
    @api.expect(update_model)
    def put(self, userId, ticketID):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        status = logic['base'].update(request.data, ticketID)
        if status != 200:
            return {},status
        x = threading.Thread(target=logic['pub'].updated, args=(ticketID,))
        x.start()
        #logic['pub'].updated(ticketID)
        return {}, status

@api.route("/callback/")
class Callback(Resource):

    @api.expect(callback_model)		
    def post(self):
        return {'status': 200}


@api.route('/unused')
class Placeholder(Resource):
    @jwt_required()
    @api.expect(content_model)
    def get(self):
        return {}, 404


