import pytest
import os, sys, inspect 

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from main import flask_app
import pytest

from  mongo_fixtures import * 


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
