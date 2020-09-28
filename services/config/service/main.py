from startup import *
from flask_restplus import  Resource, marshal_with
from flask_cors import CORS, cross_origin
from models.models import msg_model, sub_model, pub_model
from logic.logic import *
from flask import request
from flask_jwt_extended import (jwt_required, get_jwt_identity)


@api.route("/")
class Base(Resource):
	
	def post(self):
		return {'status': 200 }

	def get(self):
		return {'status': 200}	
