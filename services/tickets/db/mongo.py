from db.iticketdb import ITicketDatabase 
from pymongo import MongoClient
from interface import implements


class MongoDatabase(implements(ITicketDatabase)):

	def setup(self):
		client = MongoClient('mongodb://localhost:27017/')
		self.db = client.ticketdb


	def __init__(self):
		ITicketDatabase.__init__(self)
		
	def update(self, criteria, ticket):
		self.db.ticket.update_one(criteria, { '$set' : ticket})

	def delete(self, ticketID):
		self.db.ticket.delete_one({'id': ticketID})

	def create(self, ticket):
		print(ticket)
		self.db.ticket.insert(ticket)

	def get(self):
		cursor = self.db.ticket.find()
		tickets =  [ t for t in cursor]
		for t in tickets:
			del t['_id']
		return tickets
		
	
