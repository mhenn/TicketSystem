from flask import Flask
from flask_restx import Api 
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import requests
import time

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




class FlaskSetup:

    def __init__(self, name, m_name):
        description = f'{name} API'

        authorizations = {
            'Bearer Auth': {
                'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
            },
        }

        flask_app = Flask(m_name)
        
        flask_app.config['JWT_ALGORITHM'] = 'RS256'
        flask_app.config['JWT_PUBLIC_KEY'] = get_pubkey()
        CORS(flask_app)

        self.app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
        self.api = self.app.namespace(name, description=description)

        self.jwt = JWTManager(flask_app)
        self.flask_app = flask_app

    def get_mandatory(self):
        return self.jwt, self.api, self.flask_app, self.app

