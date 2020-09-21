from db.mongo import *
from logic.ilogic import ILogic
from interface import implements


class Logic(implements(ILogic)):

	def __init__(self, db):
		self.db = db

	def delete(self, ticketID):
		self.db.delete(ticketID)


	def update(self, ticket):
		self.db.update( ticket)


	def create(self, ticket):
		self.db.create(ticket)
	
	
	def get(self):
		return self.db.get()
