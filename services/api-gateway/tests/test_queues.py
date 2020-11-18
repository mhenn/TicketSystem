import json
import responses
#get

url = '/gateway/queues/'

@responses.activate
def test_queues_get(app, client):
    responses.add(responses.GET, 'http://localhost:5555/config/queues/',
            body=b'{"queues": []}', status=200)
    res = client.get(url)

    assert res.status_code == 200


