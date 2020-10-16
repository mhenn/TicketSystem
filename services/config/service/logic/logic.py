from db.mongo import *
import requests
import json 

class QueueLogic():

    def __init__(self, db):
        self.db = db

    def create(self, queue):
        self.db.create_queue(queue)

    def delete(self, queueId):
        self.db.delete_queue(queueId)

    def get(self):
        return self.db.get_queues()
