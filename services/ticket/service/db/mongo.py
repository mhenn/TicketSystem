from pymongo import MongoClient
from bson import ObjectId

class MongoDatabase():

    def setup(self):
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client.ticketdb


    def __init__(self):
        self.setup()


    def update(self, ticket, id):
        print(type(ticket))
        return self.db.ticket.update_one({'_id': ObjectId(id)}, { '$set' : ticket})

    def delete(self, ticketID):
        return self.db.ticket.delete_one({'_id': ObjectId(ticketID)})

    def create(self, ticket):
        if 'id' in ticket:
            del ticket['id']
        return self.db.ticket.insert(ticket)

    def get(self, criteria):
        cursor = self.db.ticket.find(criteria)

        tickets =  [ t for t in cursor]
        for t in tickets:
            t['id'] = str(t['_id'])
            del t['_id']
        return tickets


    def get_all(self):
        cursor = self.db.ticket.find()
        tickets =  [ t for t in cursor]
        for t in tickets:
            t['id'] = str(t['_id'])
            del t['_id']
        return tickets


