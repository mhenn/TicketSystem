from db.mongo import *
import json
import os

class Logic():

	def __init__(self, db):
		self.db = db
		
	def delete(self, ticketID):
		self.db.delete(ticketID)

	def createFiles(self, files, uid, ticketId, messageId):
		path = f'./files/{uid}/{ticketId}/{messageId}'
		
		if not os.path.isdir(path):
			os.makedirs(path)

		for f in files:
			f.save(path)
		

	def update(self, ticket, ticketID):
		ticket = json.loads(ticket)
		self.db.update(ticket, ticketID)


	def create(self, ticket):
		ticket['status'] = 'open'
		return self.db.create(ticket)
	
	
	def get(self):
		return self.db.get()
	
