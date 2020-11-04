import os, sys, inspect 
import unittest

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from startup import flask_app, service
app = flask_app
class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.token = service
        
    def test_get(self):
        rv = self.app.get('ticket/123')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
