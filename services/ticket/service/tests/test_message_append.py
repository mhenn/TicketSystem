import json
from utils import * 
import responses


def get_url(tid):
    return '/ticket-service/ticket/' + tid

url = 'http://localhost:5050/ticket-service/ticket'

@responses.activate
def test_message_put(app,client, insert_ticket):
   
    ticket = insert_ticket[0]
    responses.add(responses.PUT,url  , status=200)
    content = {'timestamp':"time", 'message':'Message', 'appendices': [{}] }

    res = client.put(get_url( ticket['id']), data=json.dumps(content))
    d = insert_ticket[1]
    count = d.ticket.count_documents({})
    cursor = d.ticket.find()
    del ticket['id']
    assert res.status_code == 200
    assert count == 1
    assert_list([ticket], cursor)


def test_message_put_wrong_id(app,client, insert_ticket):

    content = {'timestamp':"time", 'message':'Message', 'appendices': [{}]}
    ticket = insert_ticket[0]
    res = client.put(get_url('123'), data=json.dumps(content))
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 409


def test_message_put_wrong(app,client, insert_ticket):
    ticket = insert_ticket[0]
    res = client.put(get_url(ticket['id']), data='{"caption":"test"}')
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 400 
    assert count == 1 

def test_message_put_empty(app, client, insert_ticket):
    ticket = insert_ticket[0]
    res = client.put(get_url(ticket['id']), data='')
    d = insert_ticket[1] 
    count = d.ticket.count_documents({})
    assert res.status_code == 400
    assert count == 1


