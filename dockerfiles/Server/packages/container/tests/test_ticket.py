import json
from utils import * 
import responses
import pytest

from logic.logic import Ticket, Logic
# /tickets/
#get
from utils import assert_list, assert_map

def get_url(uid):
    return '/ticket-service/user/'+ uid

#VAGUE
#POST
url = 'http://localhost:5025/mail-service/'

@responses.activate
def test_tickets_post(app,client):
   
    ticket_url = 'http://localhost:5000/ticket-service/ticket/1'
    file_url = 'http://localhost:5000/ticket-service/user/234/ticket/1/message/Tue,03Nov202012:33:19GMT/file/hello_parse.cpp'
#    responses.add(responses.POST, url , status=200)

    ticket = {'ticket': [{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'A01_1', 'to': 'A01_1','uid': '234', 'messages': [{'appendices': ['hello_parse.cpp'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}]}

    responses.add(responses.GET, ticket_url , status=200, body=json.dumps(ticket))

    with open("./tests/files/hello_parse.cpp", "rb") as cpp:
        responses.add(
            responses.GET,
            file_url,
            body=cpp.read(),
            status=200,
#            content_type="image/jpeg",
            stream=True,
        )

    responses.add(responses.PUT, ticket_url, status=200)

    data = {'message': {'ticketId': '1', 'actions': 'create' }} 
    res = client.post(url, data=json.dumps(data))
    assert res.status_code == 200


#METHODS TICKET

ticket_url = 'http://localhost:5000/ticket-service/ticket/1'

@pytest.fixture
def get_ticket():
    ticket = {'ticket': [{'id': '1', 'sender': 'tester', 'status': 'open', 'subject': 'A01_1', 'to': 'A01_1','uid': '234', 'messages': [{'appendices': ['hello_parse.cpp'], 'message':'asfd', 'timestamp': 'Tue, 03 Nov 2020 12:33:19 GMT'}]}]}
    responses.add(responses.GET, ticket_url , status=200, body=json.dumps(ticket))
    return ticket


@pytest.fixture
@responses.activate
def ini_ticket(get_ticket):
    print(get_ticket['ticket'][0]['id'])
    return Ticket(get_ticket['ticket'][0]['id']), get_ticket

@responses.activate
def test_get_ticket(ini_ticket):
    ticket, data = ini_ticket
    assert_map(ticket.ticket, data['ticket'][0])

#TODO add negative cases

@responses.activate
def test_new(ini_ticket):
    content = 'message'
    msg = ini_ticket.new_(content)
    assert msg['message'] == content
    assert msg['appendices'] == [{}]


#METHODS LOGIC



   # assert msg['message'] == content
#def test_tickets_post_wrong(app,client):
#    res = client.post(url, data='{"caption":"test"}')
#    assert res.status_code == 400

#def test_tickets_post_empty(app, client):
#    res = client.post(url, data='')
#    assert res.status_code == 400

