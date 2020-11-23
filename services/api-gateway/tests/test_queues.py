import json
import responses
#get

url = '/gateway/queues/'

@responses.activate
def test_queues_get(app, client):
    responses.add(responses.GET, 'http://localhost:5555/config/queues/',
            body=b'{"queues": []}', status=200)
    res = client.get(url)
    queue = json.loads(res.data)['queues']
    assert len(queue) == 0
    assert res.status_code == 200


@responses.activate
def test_queues_with_data(app, client):
    
    queue_data = {'id':'1', 'title':'test'}
    data = {'queues': [queue_data]}
    

    responses.add(responses.GET, 'http://localhost:5555/config/queues/',
            body=json.dumps(data), status=200)
    res = client.get(url)
    queue = json.loads(res.data)['queues'][0]

    assert res.status_code == 200
    for k in queue_data:
        assert queue_data[k] == queue[k]


@responses.activate
def test_queues_with_multiple(app, client):
    
    queue_data = [{'id':'1', 'title':'test'},{'id':'2', 'title':'test2'}]
    data = {'queues': queue_data}
    

    responses.add(responses.GET, 'http://localhost:5555/config/queues/',
            body=json.dumps(data), status=200)
    res = client.get(url)
    queue = json.loads(res.data)['queues']
    print(queue)
    assert res.status_code == 200
    for q in range(len(queue_data)):
        for k in queue_data[q]:
            assert queue_data[q][k] == queue[q][k]
