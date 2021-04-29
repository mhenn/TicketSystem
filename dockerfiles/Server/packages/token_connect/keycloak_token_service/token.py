import json 
import time 
import os

import requests
import threading
from keycloak_token_service.decorators.singleton import Singleton

@Singleton
class ServiceToken:

#    def __init__(self, uname, pw, client_id):
    def __init__(self):
        self.duration = 250
        self.time_received = 0
        self._access_token = ''	
        self._updating = False
        self._uname = 'mhenn' 
        self._pw = 'mhenn'
        self._client_id = 'ticket_client'

    def update_token(self):
        current_time = time.time() -self.time_received 	
        
        j_response = ''
        url = 'http://odonata.keycloak:8080/auth/realms/Odonata/protocol/openid-connect/token'

        if not self._access_token: 
            data= {'grant_type': 'password', 'client_id': self._client_id, 'username': self._uname, 'password':self._pw}
            response = requests.post(url, data=data)
            if response.status_code != 200:
                return False

            j_response = response.json() 
            self.duration = j_response['expires_in']

        elif current_time >= self.duration:
            data = {'grant_type': 'refresh_token', 'client_id': self._client_id, 'refresh_token': self._refresh_token}
            r = requests.post(url, data=data)
            j_response = r.json()


        if j_response:	
            self.time_received = time.time()
            self._access_token = j_response['access_token']
            self._refresh_token = j_response['refresh_token']
        
        timer = threading.Timer(self.duration, self.update_token)
        timer.setDaemon(True)
        timer.start()



    def get(self):
        if not self._updating:
            self._updating = True
            self.update_token()
        return self._access_token
