from db.idb import IDatabase 
from pymongo import MongoClient
from interface import implements
from bson import ObjectId

class MongoDatabase(implements(IDatabase)):

    def setup(self):
        client = MongoClient('mongodb://localhost:27070/')
        self.db = client.pubsub


    def __init__(self):
        IDatabase.__init__(self)
		

    def create(self, publisher):
        self.db.pub.insert({'name':publisher, 'subscribers':[]})	

		
    def delete_publisher(self, publisher):
        #subscribers should be notified, so maybe we need a umount callback for subs
        pass

    def delete_subscriber(self, publisher, subscriber):
        pub = self.get_publisher(publisher)
        pub['subscribers'] = list(filter(lambda x : x['subscriber'] != subscriber, pub['subscribers']))
        self.db.pub.update({'name': publisher}, {'$set' : pub})
	
		
    def get_publishers(self):
        pubs = [ t for t in  self.db.pub.find() ]
        for p in pubs:
            del p['_id']
        return pubs	

    def get_publisher(self, publisher):
        pub = self.db.pub.find_one({'name': publisher}) 
        del pub['_id']
        return pub


    def get_subscriber(self, publisher, subscriber):
        pub = self.get_publisher(publisher)
        sub = list(filter(lambda x : x['subscriber'] == subscriber, pub['subscribers']))
        if len(sub) == 0:
            raise ValueError('No such Subscriber found')
        else: 
            return sub[0]
		

    def add_subscriber(self, publisher,sub):
        pub = self.get_publisher(publisher)
        pub['subscribers'].append(sub)
        self.db.pub.update({'name' : publisher}, {'$set': pub})
		
    def delete(self, ticketID):
        self.db.pub.delete_one({'_id': ObjectId(ticketID)})



