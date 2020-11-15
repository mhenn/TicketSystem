import pytest
import os, sys, inspect 

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


import mongomock
from unittest.mock import patch
from db.mongo import *
from logic.logic import *
from main import flask_app


@pytest.fixture
def app(monkeypatch):
    mongrel =  MongoDatabase(mongomock.MongoClient().db)
    monkeypatch.setattr('db.mongo.MongoDatabase', mongrel) 
    monkeypatch.setattr('startup.mongo', lambda: mongrel)
    monkeypatch.setattr('startup.getLogic', lambda: {'queue': iQueueLogic(mongrel)})
    yield flask_app

@pytest.fixture
def client(app, monkeypatch):
    print(dir(app))
    return app.test_client()
