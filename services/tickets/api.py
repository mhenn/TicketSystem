from flask import Flask
from flask_restplus import Api


flask_app = Flask(__name__)
app = Api(app = flask_app)

api = app.namespace('ticket', description='Ticket API')

