from db.mongo import *
from logic.ilogic import ILogic
from interface import implements
import json

class Logic(implements(ILogic)):

	def __init__(self, db):
		self.db = db


	def delete(self, ticketID):
		self.db.delete(ticketID)


	def update(self, ticket, ticketID):
		ticket = json.loads(ticket)
		self.db.update(ticket, ticketID)


	def create(self, ticket):

		ticket = json.loads(ticket)
		ticket['status'] = 'open'
		self.db.create(ticket)
	
	
	def get(self):
		return self.db.get()
	
