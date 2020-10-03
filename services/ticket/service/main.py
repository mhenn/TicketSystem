from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.ticket import  content_model, ticket_model, callback_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
import requests
import json


@api.route('/upload/')
class Upload(Resource):

	def post(self):
		print(f'req: {request} form: {request.form.to_dict()} files: {request.files.to_dict()} header: {request.headers}')
		files = request.files.to_dict()
		form = request.form.to_dict()
		logic.createFiles(files, form)
		#print(uploaded_file.filename)
		#uploaded_file.save(f'./files/{uploaded_file.filename}')
		return {'status':200}

@api.route("/")
class TicketClass(Resource):

	@jwt_required	
	@api.expect(ticket_model)
	def post(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		id = logic.create(json.loads(request.data))
		return {'status': 200, 'id': str(id)}

	@jwt_required
	def get(self):
		tickets = logic.get()
		return {'status': 200, 'tickets': tickets}

@api.route("/<string:ticketID>")
class TicketID(Resource):
	@jwt_required
	def delete(self, ticketID):
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


