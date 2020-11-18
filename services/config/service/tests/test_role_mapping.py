import json
# /queues/
#get

url = '/config/queues/'

def test_queues_get_one_queue(app, client, insert_queue):
    res = client.get(url)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == 1
    assert queues[0]['title'] == insert_queue[0]['title']

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

def test_queues_post(app,client, db_config):
   
    res = client.post(url, data='{"title":"test"}')
    assert res.status_code == 200

def test_queues_post_wrong(app,client, db_config):
    res = client.post(url, data='{"caption":"test"}')
    assert res.status_code == 400

def test_queues_post_empty(app, client, db_config):
    res = client.post(url, data='')
    assert res.status_code == 400


