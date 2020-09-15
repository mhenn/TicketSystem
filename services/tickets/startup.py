from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from flask_jwt_oidc import AuthError, JwtManager
from flask_jwt_extended import JWTManager
#from flask_oidc import OpenIDConnect

from config import Config
from db.mongo import MongoDatabase
from logic.logic import Logic


name = 'ticket'
description = 'Ticket API'

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}


flask_app = Flask(__name__)

flask_app.config['JWT_ALGORITHM'] = 'RS256'
flask_app.config['JWT_IDENTITY_CLAIM'] = 'sub'
flask_app.config['JWT_PUBLIC_KEY'] =  """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAslHDNkPEF4Xmjz8yd16l
UG15Bhr2YLkh8v6D9OCEvCNRsDq2JFqbAcxCfRnXIKjs/7n2Dv6jaU0X8FP6noEf
GHPyhlLJb/mIk/rTSEatZy0Mf/cbBkF90sJX5dilh/yCn5ygICqJ0egyQJhnrF7w
lp4JnJ2sCXySUaPmX0DyJPfhPuDMT17HktGD+F8e5SbDK8yGeoxqfkdhw5GnSzvI
poCMoSX4h8JUWUevZvKikFI377uuBDkjsuI4D6Mj5BKU7Up6cW/fsKHAWt71s1c0
B2U9tf7FIlN4r5xXSRlk0IKZ9NIvEAr3k3JIFrZQeThu9ITM66Rne9Ndh1HoIOEY
6QIDAQAB
-----END PUBLIC KEY-----"""

flask_app.config['JWT_DECODE_AUDIENCE'] = 'account'

jwt = JWTManager(flask_app)


CORS(flask_app)
app = Api(flask_app, security='Bearer Auth', authorizations=authorizations)
api = app.namespace(name, description=description)



def setupLogic(db):
	return Logic(db)

def setupDB():
	return MongoDatabase()	


def setup():
	db = setupDB()
	logic = setupLogic(db)
	return   logic


logic = setup()
