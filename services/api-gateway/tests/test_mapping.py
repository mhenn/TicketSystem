import json
import responses

def assert_list(orig, response):
    for i in range(len(orig)):
        for k in orig[i]:
            assert orig[i][k] == response[i][k]

#get



url = '/gateway/config/role-mapping/'
mapping_url = 'http://localhost:5555/config/role-mapping'

@responses.activate
def test_mappings_get(app, client):
    mapping = []
    data = {'mapping': mapping}

    responses.add(responses.GET, mapping_url,
            body=json.dumps(data), status=200)
    res = client.get(url)
    
    r_ticket = json.loads(res.data)['mapping']
    assert len(r_ticket) == 0
    assert res.status_code == 200
    


@responses.activate
def test_mappings_get_response_ticket(app, client):
    mapping = [{'id':'1','name':'test1', 'children': []}]
    data = {'mapping': mapping}

    responses.add(responses.GET, mapping_url,
            body=json.dumps(data), status=200)
    
    res = client.get(url)    
    r = json.loads(res.data)['mapping']
    assert len(r) == 1 
    assert res.status_code == 200
    assert_list(mapping, r) 


@responses.activate
def test_mappings_get_response_multiple(app, client):
    mapping = {'id':'1','name':'test1', 'children': []},{'id':'2', 'name':'test2', 'children': ['t1']},{'id': '3', 'name':'test3', 'children': ['t1', 't2']} 
    data = {'mapping': mapping}

    responses.add(responses.GET, mapping_url,
            body=json.dumps(data), status=200)
    res = client.get(url)
    r = json.loads(res.data)['mapping']
    assert len(r) == len(mapping) 
    assert res.status_code == 200
    assert_list(mapping, r) 


@responses.activate
def test_mappings_get_response_timeout(app, client): 
    res = client.get(url)    
    assert res.status_code == 502

@responses.activate
def test_mappings_get_response_error(app, client):
 
    responses.add(responses.GET, mapping_url,
            body=json.dumps({}), status=409)
       
    res = client.get(url)    
    assert res.status_code == 502
