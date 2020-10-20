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


class MappingLogic():

    def __init__(self, db):
        self.db = db

    def create(self, mapping):
        self.db.create_mapping(mapping)

    def delete(self, mappingId):
        self.db.delete_mapping(mappingId)


    def get(self):
        return self.db.get_mappings()
