from pymongo import MongoClient
from bson import ObjectId

class MongoDatabase():

    def __init__(self):	
        client = MongoClient('mongodb://localhost:27070/')
        self.db = client.pubsub

    def create(self, publisher):
        if  self.get_publisher(publisher):
            raise {'msg':"publisher already existing", 'status': 409}
        self.db.pub.insert_one({'publisher':publisher, 'subscribers':[]})	

		
    def delete_publisher(self, publisher):
        #subscribers should be notified, so maybe we need a umount callback for subs
        pass

    def delete_subscriber(self, publisher, subscriber):
        pub = self.get_publisher(publisher)
        pub['subscribers'] = list(filter(lambda x : x['subscriber'] != subscriber, pub['subscribers']))
        self.db.pub.update({'publisher': publisher}, {'$set' : pub})
	
		
    def get_publishers(self):
        pubs = [ t for t in  self.db.pub.find() ]
        if not pubs:
            raise "No publishers found"
        for p in pubs:
            del p['_id']
        return pubs	

    def get_publisher(self, publisher):
        pub = self.db.pub.find_one({'publisher': publisher}) 
        if not pub:
            raise "No such publisher found"
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
        self.db.pub.update({'publisher' : publisher}, {'$set': pub})
		
    def delete(self, ticketID):
        self.db.pub.delete_one({'_id': ObjectId(ticketID)})



