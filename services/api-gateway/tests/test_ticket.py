import json
import responses

def assert_list(orig, response):
    for i in range(len(orig)):
        for k in orig[i]:
            assert orig[i][k] == response[i][k]

#get



url = '/gateway/ticket/'
ticket_url = 'http://localhost:5000/ticket-service/user/None'

@responses.activate
def test_tickets_get(app, client):
    tickets = []
    data = {'tickets': tickets}

    responses.add(responses.GET, ticket_url,
            body=json.dumps(data), status=200)
    res = client.get(url)
    
    r_ticket = json.loads(res.data)['tickets']
    assert len(r_ticket) == 0
    assert res.status_code == 200
    


@responses.activate
def test_tickets_get_response_ticket(app, client):
    tickets = [{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []}]
    data = {'tickets': tickets}

    responses.add(responses.GET, ticket_url,
            body=json.dumps(data), status=200)
    
    res = client.get(url)    
    r_ticket = json.loads(res.data)['tickets']
    assert len(r_ticket) == 1 
    assert res.status_code == 200
    assert_list(tickets, r_ticket) 


@responses.activate
def test_tickets_get_response_multiple(app, client):
    tickets = [
            {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': []},
            {'id': '2', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}
            ]
    data = {'tickets': tickets}

    responses.add(responses.GET, ticket_url,
            body=json.dumps(data), status=200)
    res = client.get(url)
    r_ticket = json.loads(res.data)['tickets']
    assert len(r_ticket) == len(tickets) 
    assert res.status_code == 200
    assert_list(tickets, r_ticket) 


@responses.activate
def test_tickets_get_response_timeout(app, client): 
    res = client.get(url)    
    assert res.status_code == 502

@responses.activate
def test_tickets_get_response_error(app, client):
 
    responses.add(responses.GET, ticket_url,
            body=json.dumps({}), status=409)
       
    res = client.get(url)    
    assert res.status_code == 502

#POST

@responses.activate
def test_ticket_post_working(app, client):
    data = {'id': '1'}
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}

    responses.add(responses.POST, ticket_url,
            body=json.dumps(data), status=200)
    res = client.post(url, data=json.dumps(ticket))
    r_ticket = json.loads(res.data)
    assert res.status_code == 200
    assert r_ticket['id'] == '1'


@responses.activate
def test_ticket_post_wrong_data(app, client):
    data = {'id': '1'}
    
    responses.add(responses.POST, ticket_url,
            body=json.dumps(data), status=200)
    res = client.post(url, data=json.dumps(data))
    r_ticket = json.loads(res.data)
    assert res.status_code == 400


@responses.activate
def test_ticket_post_timeout(app, client):
    data = {'id': '1'}
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}

    res = client.post(url, data=json.dumps(ticket))
    r_ticket = json.loads(res.data)
    assert res.status_code == 502


@responses.activate
def test_ticket_post_error(app, client):
    data = {'id': '1'}
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}

    responses.add(responses.POST, ticket_url,
            body=json.dumps(data), status=400)
    res = client.post(url, data=json.dumps(ticket))
    r_ticket = json.loads(res.data)
    assert res.status_code == 502 


##PUT

put_url = ticket_url +'/ticket/1'

@responses.activate
def test_ticket_put_working(app, client):
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}
    data = {'ticket': ticket}
    responses.add(responses.PUT, put_url ,
            body=json.dumps(data), status=200)
    res = client.put(url+"1", data=json.dumps(data))
    r_ticket = json.loads(res.data)
    assert res.status_code == 200


@responses.activate
def test_ticket_put_wrong_data(app, client):
    data = {'id': '1'}
    
    responses.add(responses.PUT, put_url,
            body=json.dumps(data), status=200)
    res = client.put(url+'1', data=json.dumps(data))
    r_ticket = json.loads(res.data)
    assert res.status_code == 400


@responses.activate
def test_ticket_put_timeout(app, client):
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}

    data = {'ticket': ticket}
    res = client.put(url+'1', data=json.dumps(data))
    r_ticket = json.loads(res.data)
    assert res.status_code == 502


@responses.activate
def test_ticket_put_error(app, client):
    ticket = {'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'test1', 'to': 'test_receiver','uid': '234', 'messages': [{'appendices': ['asd.json'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}

    data = {'ticket': ticket}
    responses.add(responses.PUT, put_url,
             status=400)
    res = client.put(url+'1', data=json.dumps(data))
    r_ticket = json.loads(res.data)
    assert res.status_code == 502 


