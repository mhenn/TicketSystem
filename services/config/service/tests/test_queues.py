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
    assert queues[0]['id'] == insert_queue[0]['_id']

def test_queues_get_many_queues(app, client, insert_multiple_queues):
    res = client.get(url)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == len(insert_multiple_queues[0])

def test_queues_get_no_queues(app, client, insert_no_queues):
    res = client.get(url)
    print(res.data)
    queues = json.loads(res.data)['queues']
    assert res.status_code == 200
    assert len(queues) == 0
    

#POST

def test_queues_post(app,client, db_config):
    
    res = client.post(url, data='dict')
    
    assert res.status_code == 200



