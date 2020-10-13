from db.mongo import *
import json
import os

class Logic():

    def __init__(self, db):
        self.db = db
	    
    def delete(self, ticketID):
        self.db.delete(ticketID)

    def createFiles(self, files, uid, ticketId, messageId):
        path = f'./files/{uid}/{ticketId}/{messageId}/'
			    
        if not os.path.isdir(path):
            os.makedirs(path)

        for f in files:
            files[f].save(path+ f)
	    

    def update(self, ticket, ticketID):
        ticket = json.loads(ticket)
        self.db.update(ticket, ticketID)


    def create(self, ticket, uid):
        ticket['status'] = 'open'
        ticket['uid'] = uid
        return self.db.create(ticket)
	    
    def get_all(self):
        return self.db.get()
    
    
    def get(self, uid):
        return self.db.get(uid)
    
