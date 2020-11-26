import json
from utils import * 
import responses
# /tickets/
#get

#TESTING TicketClass

def get_url(uid):
    return '/ticket-service/user/'+ uid

url = '/ticket-service/ticket/'
def test_t_b_id_get_with_one(app, client, insert_ticket):
    
    res = client.get(get_url('234'))
    data = json.loads(res.data)['tickets']
    print(data)
    print(insert_ticket[0])
    assert res.status_code == 200
    assert len(data) == 1
    assert_list([insert_ticket[0]], data)

def test_tickets_get_many_tickets(app, client, insert_multiple_tickets):
    res = client.get(get_url('234'))
    tickets = json.loads(res.data)['tickets']
    assert res.status_code == 200
    assert len(tickets) == len(insert_multiple_tickets[0]) 
    assert_list(insert_multiple_tickets[0], tickets)

def test_tickets_get_no_tickets(app, client, insert_nothing):
    res = client.get(get_url('234'))
    print(res.data)
    tickets = json.loads(res.data)['tickets']
    assert res.status_code == 200
    assert len(tickets) == 0
    

#POST
pubsub_url = 'http://localhost:5050/pubsub/ticket'

@responses.activate
def test_tickets_post(app,client, insert_nothing):
   

    responses.add(responses.POST, pubsub_url , status=200)

    ticket =  { 'sender': 'tester',  'subject': 'test1', 'to': 'test_receiver', 'messages': []}
    
    res = client.post(get_url('234'), data=json.dumps(ticket))
    d = insert_nothing
    count = d.ticket.count_documents({})
    cursor = d.ticket.find()
    print(res.data)
    assert res.status_code == 200
    assert count == 1
    assert_list([ticket], cursor)

def test_tickets_post_wrong(app,client, insert_nothing):
    res = client.post(get_url('234'), data='{"caption":"test"}')
    d = insert_nothing
    count = d.ticket.count_documents({})
    assert res.status_code == 400
    assert count == 0

def test_tickets_post_empty(app, client, insert_nothing):
    res = client.post(get_url('234'), data='')
    d = insert_nothing
    count = d.ticket.count_documents({})
    assert res.status_code == 400
    assert count == 0




#url = '/ticket-service/ticket/'
#TODO ALSO NOT POSSIBLE WITH MONGOMOCK, fucking hell
#def test_t_b_id_get_with_one(app, client, insert_ticket):
#    
#    res = client.get(url+'1fb571a1985d6e7f8ca10e22')
#    data = json.loads(res.data)['ticket']
#    print(res)
#    print(data)
#    assert res.status_code == 200
#    assert len(data) == 1
#
#def test_tickets_get_many_tickets(app, client, insert_multiple_tickets):
#    res = client.get(url+ '1fb571a1985d6e7f8ca10e22')
#    tickets = json.loads(res.data)['ticket']
#    assert res.status_code == 200
#    assert len(tickets) == 1 
#
#def test_tickets_get_no_tickets(app, client, insert_nothing):
#    res = client.get(url + '1fb571a1985d6e7f8ca10e22')
#    print(res.data)
#    tickets = json.loads(res.data)['ticket']
#    assert res.status_code == 200
#    assert len(tickets) == 0
#    
#
