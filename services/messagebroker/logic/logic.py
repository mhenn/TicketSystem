from db.mongo import *
import requests
import json 

class PublisherLogic():

    def __init__(self, db):
        self.db = db

    def get_publisher(self, publisher):
        return self.db.get_publisher(publisher)

    def add_subscriber(self, publisher, sub):
        self.db.add_subscriber(publisher, sub)

    def delete_publisher(self, publisher):
        self.db.delete_publisher(publisher)

    def send_msg(self, publisher, content):
        pub = self.db.get_publisher(publisher)
        for sub in pub['subscribers']:
            print(json.dumps({'message':content}))
            requests.post(sub['callback'], data={'message':content})	


class PubSubscriberLogic():

    def __init__(self, db):
        self.db = db

    def get_subscriber(self, publisher, subscriber):
        return self.db.get_subscriber(publisher,subscriber)

    def delete_subscriber(self, publisher, subscriber):
        self.db.delete_subscriber(publisher, subscriber)

class SubscriberLogic():

    def __init__(self, db):
        self.db = db

    def get_subscriber(self, subscriber):
        pass

    def delete_subscriber(self, subscriber):
        pass


class BaseLogic():

    def __init__(self, db):
        self.db = db

    def create_publisher(self, data):
        publisher = data['publisher']
        self.db.create(publisher)

    def get_publishers(self):
        return self.db.get_publishers()
