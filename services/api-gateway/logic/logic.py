import requests
import json 
import time 
import os

from flask import Response
from flask import stream_with_context

class Logic:

    def __init__(self):
        self.service_token = ServiceToken()	

    def get_ticket(self, uid):         
        token = self.service_token.get()
        header = {'Authorization': 'Bearer ' + token }
        r = requests.get(f'http://localhost:5000/ticket-service/user/{uid}' , headers=header)		
        return r.json()['tickets']


    def post_ticket(self, ticket, uid):	
        token = self.service_token.get()
        header = {
            'Authorization': 'Bearer ' + token,
            'content-type' : 'application/json'
        }
        print(ticket)
        r = requests.post(f'http://localhost:5000/ticket-service/user/{uid}', headers=header, data=json.dumps(ticket))	
        print(r.json())
        return r.status_code, r.json()['id']

    def put_ticket(self, ticketId, ticket):	
        ticket = json.loads(ticket)
        token = self.service_token.get()
        ticket = ticket['ticket']
        header = {
            'Authorization': 'Bearer ' + token,
            'content-type' : 'application/json'
        }
        print(ticket)
        r = requests.put(f'http://localhost:5000/ticket-service/ticket/{ticketId}', headers=header, data=json.dumps(ticket))	
        return r.status_code


    def post_files(self, ticketId, uid, messageId, files):
        token = self.service_token.get()
        data = {'uid': uid}

        headers = {
            'Authorization': 'Bearer ' + token,
        }	
        r = requests.post(f'http://localhost:5000/ticket-service/ticket/{ticketId}/message/{messageId}', headers=headers,data=data, files=files)
        print(r)
        return r.status_code	

    def get_file(self, ticketId, messageId, filename, uid):
        token = self.service_token.get()
        headers = {
            "Authorization" : 'Bearer ' + token
        }
        r = requests.get(f'http://localhost:5000/ticket-service/user/{uid}/ticket/{ticketId}/message/{messageId}/file/{filename}', headers=headers)
        print(r.headers)	
        return Response(r, content_type=r.headers['Content-Type']) 


    def get_queues(self):
        token = self.service_token.get()
        headers = {
            "Authorization" : 'Bearer ' + token
        }   
        r = requests.get('http://localhost:5555/config/queues/', headers=headers)
        return r.json()['queues']
        



class ServiceToken:

    def __init__(self):
        self.duration = 250
        self.time_received = 0
        self._access_token = ''	

    def get(self):

        current_time = time.time() -self.time_received 	
        j_response = ''
        url = 'http://localhost:8000/auth/realms/Odonata/protocol/openid-connect/token'

        if not self._access_token: 
            data= {'grant_type': 'password', 'client_id':'ticket-client', 'username':'mhenn', 'password':'mhenn'}
            response = requests.post(url, data=data)
            if response.status_code != 200:
                return False

            j_response = response.json() 
            self.duration = j_response['expires_in']

        elif current_time >= self.duration:
            data = {'grant_type': 'refresh_token', 'client_id': 'ticket-client', 'refresh_token': self._refresh_token}
            r = requests.post(url, data=data)
            j_response = r.json()


        if j_response:	
            self.time_received = time.time()
            self._access_token = j_response['access_token']
            self._refresh_token = j_response['refresh_token']
        return self._access_token

