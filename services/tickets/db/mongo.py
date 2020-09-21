from db.iticketdb import ITicketDatabase 
from pymongo import MongoClient
from interface import implements
from bson import ObjectId

class MongoDatabase(implements(ITicketDatabase)):

	def setup(self):
		client = MongoClient('mongodb://localhost:27017/')
		self.db = client.ticketdb


	def __init__(self):
		ITicketDatabase.__init__(self)
		
	def update(self, ticket):
		id = ticket.id
		del ticket['id']
		self.db.ticket.update_one({'_id': ObjectId(id)}, { '$set' : ticket})

	def delete(self, ticketID):
		self.db.ticket.delete_one({'_id': ObjectId(ticketID)})

	def create(self, ticket):
		del ticket['id']
		self.db.ticket.insert(ticket)

	def get(self):
		cursor = self.db.ticket.find()
		tickets =  [ t for t in cursor]
		for t in tickets:
			t['id'] = str(t['_id'])
			del t['_id']
		return tickets
		
	
