from db.mongo import *
from logic.ilogic import ILogic
from interface import implements


class Logic(implements(ILogic)):

	def __init__(self, db):
		self.db = db

	def delete(self, ticketID):
		self.db.delete(ticketID)


	def update(self, ticket, ticketID):
		self.db.update(ticket, ticketId)


	def create(self, ticket):
		ticket['status'] = 'open'
		self.db.create(ticket)
	
	
	def get(self):
		return self.db.get()
