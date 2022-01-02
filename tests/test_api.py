import unittest
import json
from flask import current_app
from app import create_app


class APITestCase(unittest.TestCase):
    """Performs tests related to the Flask API endpoints provided"""
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None, 'Current app should exist')

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'], 'App should be in testing mode')

    def test_bad_url_requests(self):
        response = self.client.get('/invalid_path')
        self.assertEqual(response.status_code, 404, 'Invalid path should generate a 404')
        response = self.client.get('/vi/users')
        self.assertEqual(response.status_code, 404, 'Partial path should generate a 404')
        response = self.client.get('/v1/users_in_or_near/Atlantis/miles/50')
        self.assertEqual(response.status_code, 400, 'Invalid city should generate a 400')
        response = self.client.get('/v1/users_in_or_near/Kax/cubits/50')
        self.assertEqual(response.status_code, 400, 'Invalid unit should generate a 400')
        response = self.client.get('/v1/users_in_or_near/Kax/miles')
        self.assertEqual(response.status_code, 404, 'Partial path should generate a 404')
        response = self.client.get('/v1/users_in_or_near/Kax/miles/jellyfish')
        self.assertEqual(response.status_code, 400, 'Invalid distance should generate a 400')

    def test_users_near_city(self):
        response = self.client.get('/v1/users_in_or_near/Kax/miles/50')
        self.assertEqual(response.status_code, 200, 'Valid query should generate a 200 response code')
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3, 'Valid query should generate three users')
        self.assertIsInstance(json_response, list)
        id_list = [x['id'] for x in json_response]
        id_list.sort()
        self.assertEqual(id_list, [1, 2, 854], 'Valid query should generate the specified ID list')
