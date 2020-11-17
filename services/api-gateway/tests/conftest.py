import pytest
import os, sys, inspect 

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from main import *
import pytest
import pytest_mock 
from  mongo_fixtures import * 

@pytest.fixture
def app(mocker):
    mocker.patch('flask_jwt_extended.view_decorators.verify_jwt_in_request', lambda : print('verify'))
    mocker.patch('startup.service.update_token', lambda: '3')
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
