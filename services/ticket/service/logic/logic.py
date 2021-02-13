from db.mongo import *
import requests
import json
import os
from bson import ObjectId

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
        try:
            self.db.update(ticket, ticketID)
        except Exception as e:
            #TODO LOG
            print(e)
            return 409
        return 200

    def create(self, ticket, uid):
        ticket['status'] = 'open'
        ticket['uid'] = uid
        return self.db.create(ticket)
	    
    def get_all(self):
        return self.db.get_all()
    
    def get_by_uid(self,uid):
        return self.db.get({'uid': uid})

    def get_by_id(self, tId):
        try:
            return self.db.get({'_id': ObjectId(tId)}), 200
        except Exception as e:
            #TODO LOG
            print(e)
            return {}, 409

    def getTicketByTopic(self, content):
        
        tickets = []
        for topic in content['topics']:
            tickets = tickets + self.db.get({'to' : topic})
        return tickets

    def appendMessage(self, ticketId, data):
        try:
            self.db.append(data, ticketId) 
        except Exception as e:
            print(e)
            return 409
        return 200


class PubLogic():

    def __init__(self,db,ts):
        self.db = db
        self.token_service = ts

    def __send (self, oid, u_type):
        try:
            token = self.token_service.get()
            header = {'Authorization' : 'Bearer ' + token}
            data = {'message': {'actions': u_type, 'ticketId': oid}}
            requests.post('http://localhost:5050/pubsub/ticket', headers=header, data=json.dumps(data))
        except Exception as e:
            print(e)

    def updated(self, oid):
        self.__send(oid, 'updated')

    def created(self, oid):
        self.__send(oid, 'created')
        #ticket = self.db.get({'_id' : ObjectId(oid)})

