from pymongo import MongoClient
from bson import ObjectId

class MongoDatabase():

    def setup(self):
        client = MongoClient('mongodb://localhost:27000/')
        self.db = client.config


    def __init__(self):
        self.setup()

    def create_queue(self, queue):
        self.db.queue.insert(queue)	


    def delete_queue(self,  queueId):
        self.db.queue.delete_one({'_id' : ObjectId(queueId)})


    def get_queues(self):
        cursor = self.db.queue.find()
        queues = [q for q in cursor] 
        for q in queues:
            q['id'] = str(q['_id'])
            del q['_id']
        return queues


    def create_mapping(self, mapping):
        self.db.mapping.insert(mapping)	


    def delete_mapping(self,  mappingId):
        self.db.mapping.delete_one({'_id' : ObjectId(mappingId)})


    def get_mappings(self):
        cursor = self.db.mapping.find()
        mappings = [q for q in cursor] 
        for m in mappings:
            m['id'] = str(m['_id'])
            del m['_id']
        return mappings
 
    def create_mail_mapping(self,mapping):
        return self.db.mail.insert(mapping)
    
    def get_mail_mappings(self):
        cursor = self.db.mail.find()
        mappings = [q for q in cursor] 
        for m in mappings:
            m['id'] = str(m['_id'])
            del m['_id']
        return mappings
 

