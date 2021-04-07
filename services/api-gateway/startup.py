from flask import Flask
#from flask_restplus import Api
from flask_restx import Api 
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from logic.token import  ServiceToken
#from flask_oidc import OpenIDConnect
import requests
import time
from logic.logic import *


name = 'gateway'
description = 'Gateway API'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

def get_pubkey():
    for _ in range(20):
        try:
            r = requests.get('http://odonata.keycloak:8080/auth/realms/Odonata')
            break
        except Exception:
            time.sleep(5)

    r = r.json()
    return f"""-----BEGIN PUBLIC KEY-----
{r['public_key']}
-----END PUBLIC KEY-----""" 


flask_app = Flask(__name__)

flask_app.config['JWT_ALGORITHM'] = 'RS256'
#flask_app.config['JWT_IDENTITY_CLAIM'] = 'sub'
flask_app.config['JWT_PUBLIC_KEY'] = get_pubkey()
#
#"""
#MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAk5fiYnAuVDbHIM/MZ91Ws6x7ffGBIlsmKW3y9wKpnmpYR64iOG3X/wYknkC8NLsRzCluQXDKWDFQPiRpUyYQRjZxes1sDy/zOQ4gEMIasrdBLpPEqLSHTipForvCASN4NwncpFW2l2+wi8slsTTrszvA2ZM5oZXy9tI5DaklN5jI1l/1bZM6x3VcMTkvQ1+GR9ObrB7PxVMElXqYZ5h83GybVs7AdJA0QLfxcpgFr114KizuS09xWOMGgm6xPDN+8cHIBB1G1nN5K7v+jZ1Y6Ya3cjR7gXgVXxkd3cia83J//nL92grFVDAP/IBu3Ahq3vTPrT8CiosOCSLsJmSGRQIDAQAB
#"""
#
#flask_app.config['JWT_DECODE_AUDIENCE'] = 'account'




CORS(flask_app)


app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
api = app.namespace(name, description=description)

jwt = JWTManager(flask_app)

service = ServiceToken()	
logic = {'base':Logic(service), 'config': ConfigLogic(service)}

