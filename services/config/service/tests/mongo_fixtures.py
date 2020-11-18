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
    queue = {'_id':'1fb571a1985d6e7f8ca10e22', 'title':'test1'}
    db_config.queue.insert_one(queue)
    db.db = db_config
    queue['id'] = queue['_id']
    del queue['_id']
    return queue, db.db

@pytest.fixture
def insert_multiple_queues(db_config):
    test_list =[{'_id': '1fb571a1985d6e7f8ca10e22','title':'test1'},
                {'_id': '2fb571a1985d6e7f8ca10e22','title':'test2'},
                {'_id': '3fb571a1985d6e7f8ca10e22','title':'test3'}] 
    db_config.queue.insert_many(test_list)
    db.db = db_config
    for m in test_list:
        m['id'] = m['_id']
        del m['_id']
    return test_list, db.db

@pytest.fixture
def insert_nothing(db_config):
    db.db = db_config
    return db.db



#MAIL

@pytest.fixture
def insert_mail_one(db_config):
    mail = {"name": "test1", "mappingId": "1234", "type": "role", "actions": ["created"], "_id": "1"}
    db_config.mail.insert_one(mail)
    db.db = db_config
    mail['id'] = mail['_id']
    del mail['_id']
    return mail, db.db.mail

@pytest.fixture
def insert_mail_multiple(db_config):
    mail =[{"name": "test1", "mappingId": "1234", "type": "role", "actions": ["created"], "_id": "1"},{"name": "test2", "mappingId": "1234", "type": "role", "actions": ["updated"], "_id": "2"},{"name": "test3", "mappingId": "1234", "type": "role", "actions": ["created","updated"], "_id": "3"} ] 
    db_config.mail.insert_many(mail)
    db.db = db_config
    for m in mail:
        m['id'] = m['_id']
        del m['_id']
    return mail, db.db.mail


