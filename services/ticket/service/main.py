from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.ticket import  content_model, ticket_model, callback_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from werkzeug.datastructures import FileStorage
import requests
import json

upload_parser = api.parser()
upload_parser.add_argument('rat')
upload_parser.add_argument('file', location='files', type=FileStorage, required=False)

@api.route('/upload/')
@api.expect(upload_parser)
class Upload(Resource):

	def post(self):
		print(f'req: {request} form: {request.form.get("rat")} files: {request.files.get("file")} data: {request.data} header: {request.headers}')
		#args = upload_parser.parse_args()
		#print(args)
		#uploaded_file = args['file']
		#print(uploaded_file.filename)
		#uploaded_file.save(f'./files/{uploaded_file.filename}')
		return {'status':200}

@api.route("/")
class TicketClass(Resource):

	@jwt_required	
	@api.expect(ticket_model)
	def post(self):
		print(f'req: {request} data: {request.data} header: {request.headers}')
		logic.create(request.data)
		return {'status': 200 }

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


