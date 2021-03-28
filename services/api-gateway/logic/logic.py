from logic.token import ServiceToken
from flask import Response, jsonify
from flask import stream_with_context
import requests
import json

tickethost = 'odonata.ticket'
confighost = 'odonata.config'

bad_gateway = 502 

class Logic:

    def __init__(self, service):
        self.service_token = service

    def get_ticket(self, uid):         
        token = self.service_token.get()
        header = {'Authorization': 'Bearer ' + token }
        raise Exception(token + ' ' + uid)
        try:
            r = requests.get(f'http://{tickethost}:5000/ticket-service/user/{uid}' , headers=header)		
            raise Exception(r)
            if not r.ok:
                return [], bad_gateway
        except requests.exceptions.RequestException as e:
            #TODO LOG
            return [], bad_gateway
        
        return r.json()['tickets'], 200


    def post_ticket(self, ticket, uid):	
        token = self.service_token.get()
        header = {
            'Authorization': 'Bearer ' + token,
            'content-type' : 'application/json'
        }
        
        try:
            r = requests.post(f'http://{tickethost}:5000/ticket-service/user/{uid}', headers=header, data=json.dumps(ticket))	
            if not r.ok:
                return [], bad_gateway
        except requests.exceptions.RequestException as e:
            return [], bad_gateway
        return  r.json()['id'], r.status_code

    def put_ticket(self, ticketId, ticket, uid):	
        ticket = json.loads(ticket)
        token = self.service_token.get()

        ticket = ticket['ticket']
        header = {
            'Authorization': 'Bearer ' + token,
            'content-type' : 'application/json'
        }
        try:
            r = requests.put(f'http://{tickethost}:5000/ticket-service/user/{uid}/ticket/{ticketId}', headers=header, data=json.dumps(ticket))	
            if not r.ok:
                return  bad_gateway
        except requests.exceptions.RequestException as e:
            #TODO LOG
            return  bad_gateway
        return r.status_code


    def post_files(self, ticketId, uid, messageId, files):
        token = self.service_token.get()
        data = {'uid': uid}

        headers = {
            'Authorization': 'Bearer ' + token,
        }	
        r = requests.post(f'http://{tickethost}:5000/ticket-service/ticket/{ticketId}/message/{messageId}', headers=headers,data=data, files=files)
        print(r)
        return r.status_code	

    def get_file(self, ticketId, messageId, filename, uid):
        token = self.service_token.get()
        headers = {
            "Authorization" : 'Bearer ' + token
        }
        print(f'http://{tickethost}:5000/ticket-service/user/{uid}/ticket/{ticketId}/message/{messageId}/file/{filename}')
        r = requests.get(f'http://{tickethost}:5000/ticket-service/user/{uid}/ticket/{ticketId}/message/{messageId}/file/{filename}', headers=headers)
#        return Response(r.content, content_type=r.headers['Content-Type']) 
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in r.raw.headers.items()
               if name.lower() not in excluded_headers]

        if not r.ok:
            return 404

        return Response(r.content, r.status_code, headers)

    def get_queues(self):
        token = self.service_token.get()
        headers = {
            "Authorization" : 'Bearer ' + token
        }   
        r = requests.get('http://{confighost}:5555/config/queues/', headers=headers)
        return r.json()['queues']
    
    def ticket_topic(self, data):
        print(data)
        token = self.service_token.get()
        header = {
            "Authorization" : 'Bearer ' + token,
        }
        r = requests.post('http://{tickethost}:5000/ticket-service/ticket/topics/', headers=header,data=data)
        print(r)
        return json.loads(r.content)


class ConfigLogic():

    def __init__(self, service):
        self.service_token = service

    def get_mapping(self):
        token = self.service_token.get()
        header = {'Authorization': 'Bearer ' + token }
        try:    
            r = requests.get('http://{confighost}:5555/config/role-mapping', headers=header)
        
            if not r.ok:
                return  [], bad_gateway
        except requests.exceptions.RequestException as e:
            #TODO LOG
            return  [], bad_gateway
        return json.loads(r.content), 200

