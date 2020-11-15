import mongomock
import pytest

@pytest.fixture
def hello():
    print('ohla')
    return 1
