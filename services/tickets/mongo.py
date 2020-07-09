from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.ticketdb


def createTicket(ticketDTO):
	db.ticket.insert(ticketDTO)
