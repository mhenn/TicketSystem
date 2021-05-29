from db.mongo import *
import requests
import json 
import logging

class PublisherLogic():

    def __init__(self, db):
        self.db = db

    def get_publisher(self, publisher):
        try:
            return self.db.get_publisher(publisher)
        except ValueError as e:
            logging.error(e)
            return []

    def add_subscriber(self, publisher, sub):
        self.db.add_subscriber(publisher, sub)

    def delete_publisher(self, publisher):
        self.db.delete_publisher(publisher)

    def send_msg(self, publisher, content):
        try:
            pub = self.db.get_publisher(publisher)
        except ValueError as e:
            logging.error(e)
            return {'message': e}, 409
        print(pub)
        for sub in pub['subscribers']:
            try:
                requests.post(sub['callback'], data=json.dumps(content))	
            except Exception as e:
                logging.error(e)



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
        try:
            return self.db.get_publishers()
        except ValueError as e:
            logging.error(e)
            return []
