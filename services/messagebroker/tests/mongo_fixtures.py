import pytest
import mongomock
from main import db 
from db.mongo import *
from bson import ObjectId

@pytest.fixture
def db_mock():
    return  mongomock.MongoClient()

@pytest.fixture
def db_config(db_mock):
    return db_mock.pubsub

#QUEUES
@pytest.fixture
def insert_pub(db_config):
    pub = {'_id':'1', 'publisher':'test1'}
    db_config.pub.insert_one(pub)
    db.db = db_config
    return pub, db.db

@pytest.fixture
def insert_multiple_pubs(db_config):
    test_list =[{'_id': '1','publisher':'test1'},
                {'_id': '2','publisher':'test2'},
                {'_id': '3','publisher':'test3'}] 
    db_config.pub.insert_many(test_list)
    db.db = db_config
    for m in test_list:
        m['id'] = m['_id']
        del m['_id']
    return test_list, db.db

@pytest.fixture
def insert_nothing(db_config):
    db.db = db_config
    return db.db

