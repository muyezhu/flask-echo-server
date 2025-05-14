import unittest
import json
from flask_echo_server.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_echo_twice(self):
        payload = {"message": "hello"}
        response = self.app.post('/echo_twice',
                                   data=json.dumps(payload),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        expected_response = {"echo_twice": [payload, payload]}
        self.assertEqual(response.get_json(), expected_response)

if __name__ == '__main__':
    unittest.main()
