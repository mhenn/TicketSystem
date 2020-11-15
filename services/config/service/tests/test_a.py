import json 
import logic.logic as logic
from unittest.mock import patch
import mongomock
import startup
from db.mongo  import *

def test_index(app, client,monkeypatch):

    res = client.get('/config/queues/')
    print(res.data)
    assert res.status_code == 100

#def test_mail(app,client, hello):
#    res = client.get('/config/mail/')
#    assert res.status_code == 500

