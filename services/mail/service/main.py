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

@api.route('/')
class UserFileUpload(Resource):
    
    @jwt_required
    def post(self,  ticketId, messageId):
        print(f'req: {request} form: {request.form.to_dict()} files: {request.files.to_dict()} header: {request.headers}')
        # print( logic['base'].createFiles(files, form['uid'], ticketId, messageId))
        #print(uploaded_file.filename)
        #uploaded_file.save(f'./files/{uploaded_file.filename}')
        return {'status':200}


