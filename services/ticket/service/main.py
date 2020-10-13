from startup import *
from flask_restplus import  Resource, marshal_with
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

    def post(self,  ticketId, messageId):
        print(f'req: {request} form: {request.form.to_dict()} files: {request.files.to_dict()} header: {request.headers}')
        files = request.files.to_dict()
        form = request.form.to_dict()
        logic.createFiles(files, form['uid'], ticketId, messageId)
        #print(uploaded_file.filename)
        #uploaded_file.save(f'./files/{uploaded_file.filename}')
        return {'status':200}



@api.route('/user/<string:uid>/ticket/<string:ticketId>/message/<string:messageId>/file/<string:filename>')
class FileDownload(Resource):

    def get(self, ticketId, uid, messageId, filename):
        uid = 'd2717165-4f26-477b-a992-bc31b2b085cd'
        return send_from_directory(f'./files/{uid}/{ticketId}/{messageId}', filename, as_attachment=True)


@api.route("/user/<string:userId>")
class TicketClass(Resource):

    @jwt_required	
    @api.expect(ticket_model)
    def post(self, userId):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        id = logic.create(json.loads(request.data), userId)
        return {'status': 200, 'id': str(id)}

    @jwt_required
    def get(self, userId):
        tickets = logic.get(userId)
        return {'status': 200, 'tickets': tickets}


@api.route("/user/<string:userId>/ticket/<string:ticketID>")
class TicketID(Resource):
    @jwt_required
    def delete(self, userId, ticketID):
        logic.delete(ticketID)
        return {'status':200}

    @api.expect(ticket_model)
    def put(self, ticketID):
        print(f'req: {request} data: {request.data} header: {request.headers}')
        logic.update(request.data, ticketID)
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


