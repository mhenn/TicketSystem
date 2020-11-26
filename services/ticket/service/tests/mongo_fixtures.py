import pytest
import mongomock
from main import db 
from db.mongo import *
from bson import ObjectId

@pytest.fixture
def db_mock():
    return  mongomock.MongoClient()

@pytest.fixture
def db_ticket(db_mock):
    return db_mock.ticketdb

#QUEUES
@pytest.fixture
def insert_ticket(db_ticket):
    ticket =  {'_id': '1fb571a1985d6e7f8ca10e22', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []}
    db_ticket.ticket.insert_one(ticket)
    db.db = db_ticket
    ticket['id'] = ticket['_id']
    del ticket['_id']
    return ticket, db.db

@pytest.fixture
def insert_multiple_tickets(db_ticket):
    ticket = [ 
        {'_id': '1fb571a1985d6e7f8ca10e22', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
        {'_id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]},
        ]


    db_ticket.ticket.insert_many(ticket)
    db.db = db_ticket
    for m in ticket:
        m['id'] = m['_id']
        del m['_id']
    return ticket, db.db

@pytest.fixture
def insert_nothing(db_ticket):
    db.db = db_ticket
    return db.db

