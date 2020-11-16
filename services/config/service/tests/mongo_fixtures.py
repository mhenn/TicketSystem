import pytest
import mongomock
from main import db 
from db.mongo import *


@pytest.fixture
def db_mock():
    return  mongomock.MongoClient()

@pytest.fixture
def db_config(db_mock):
    return db_mock.config

#QUEUES
@pytest.fixture
def insert_queue(db_config):
    queue = {'_id': '1', 'title':'test1'}
    db_config.queue.insert_one(queue)
    db.db = db_config
    return queue, db.db

@pytest.fixture
def insert_multiple_queues(db_config):
    test_list =[{'title':'test1'},{'title':'test2'},{'title':'test3'}] 
    db_config.queue.insert_many(test_list)
    db.db = db_config
    return test_list, db.db

@pytest.fixture
def insert_no_queues(db_config):
    db.db = db_config
    return db.db



