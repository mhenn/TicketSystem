from pymongo import MongoClient
from bson import ObjectId

class MongoDatabase():


    def __init__(self, url): 
        self.db = MongoClient(url).config

    def create_queue(self, queue):
        self.db.queue.insert_one(queue)	


    def delete_queue(self,  queueId):
        ret = self.db.queue.delete_one({'_id' : ObjectId(queueId)})

    def get_queues(self):
        cursor = self.db.queue.find()
        queues = [q for q in cursor] 
        for q in queues:
            q['id'] = str(q['_id'])
            del q['_id']
        return queues


    def create_mapping(self, mapping):
        self.db.mapping.insert_one(mapping)	


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
        return self.db.mail.insert_one(mapping)
    
    def get_mail_mappings(self):
        cursor = self.db.mail.find()
        mappings = [q for q in cursor] 
        for m in mappings:
            m['id'] = str(m['_id'])
            del m['_id']
        return mappings
 

    def delete_mail_mapping(self,  mappingId):
        self.db.mail.delete_one({'_id' : ObjectId(mappingId)})

