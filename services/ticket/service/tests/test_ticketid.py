
import json
from utils import * 
import responses


def get_url(uid, tid):
    return '/ticket-service/user/'+ uid + '/ticket/' + tid

pubsub_url = 'http://localhost:5050/pubsub/ticket'

@responses.activate
def test_tickets_put(app,client, insert_ticket):
   

    ticket = insert_ticket[0]
    responses.add(responses.POST, pubsub_url , status=200)
    
    res = client.put(get_url('234', ticket['id']), data=json.dumps(ticket))
    d = insert_ticket[1]
    count = d.ticket.count_documents({})
    cursor = d.ticket.find()
    del ticket['id']
    assert res.status_code == 200
    assert count == 1
    assert_list([ticket], cursor)


def test_tickets_put_wrong_id(app,client, insert_ticket):
    ticket = insert_ticket[0]
    res = client.put(get_url('234','123'), data=json.dumps(ticket))
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 409


def test_tickets_put_wrong(app,client, insert_ticket):
    ticket = insert_ticket[0]
    res = client.put(get_url('234',ticket['id']), data='{"caption":"test"}')
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 400 
    assert count == 1 

def test_tickets_put_empty(app, client, insert_ticket):
    ticket = insert_ticket[0]
    res = client.put(get_url('234',ticket['id']), data='')
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 400
    assert count == 1


