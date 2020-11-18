import json
from main import db
# /queues/
#get

url = '/config/queues/'

def test_queues_get_one_queue(app, client, insert_queue):
    res = client.get(url)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == 1
    for k in insert_queue[0]:
        assert queues[0][k] == insert_queue[0][k]

def test_queues_get_many_queues(app, client, insert_multiple_queues):
    res = client.get(url)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == len(insert_multiple_queues[0])

def test_queues_get_no_queues(app, client, insert_nothing):
    res = client.get(url)
    print(res.data)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == 0
    

#POST

def test_queues_post(app,client, insert_nothing):
   
    res = client.post(url, data='{"title":"test"}')
    d = insert_nothing
    count = d.queue.count_documents({})
    assert res.status_code == 200
    assert count == 1


def test_queues_post_wrong(app,client, insert_nothing):
    res = client.post(url, data='{"caption":"test"}')
    d = insert_nothing
    count = d.queue.count_documents({})
    assert res.status_code == 400
    assert count == 0

def test_queues_post_empty(app, client, insert_nothing):
    res = client.post(url, data='')
    d = insert_nothing
    count = d.queue.count_documents({})
    assert res.status_code == 400
    assert count == 0

#DELETE


def test_queues_delete_with_one_queue(app, client, insert_queue):
    queue = insert_queue[0]
    res = client.delete(url+ queue['id'])
    d = insert_queue[1]
    count = d.queue.count_documents({})
    assert res.status_code == 200
    assert count == 0 


def test_queues_delete_with_multiple_queues(app, client, insert_multiple_queues):
    queue = insert_multiple_queues[0]
    res = client.delete(url+ queue[0]['id'])
    d = insert_multiple_queues[1]
    count = d.queue.count_documents({})
    assert res.status_code == 200
    assert count == len(queue ) -1

   
    
def test_queues_delete_without_any_queues(app, client, insert_nothing): 
    pass
