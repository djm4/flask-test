import unittest
import json
from flask import current_app
from app import create_app
from app.api_wrappper import APIWrapper
from app.user import User, Location


class APITestCase(unittest.TestCase):
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
        id_list = [x['id'] for x in json_response.values()]
        id_list.sort()
        self.assertEqual(id_list, [1, 2, 854], 'Valid query should generate the specified ID list')

    def test_api_wrapper(self):
        api = APIWrapper()
        self.assertIn('todo', api.instructions(), 'instructions endpoint should have todo as a key')
        user = api.user(1)
        self.assertIsInstance(user, User, 'user endpoint should return a User object')
        self.assertEqual(user.first_name, 'Maurise', 'user\'s first name should be Maurise')
        self.assertIsInstance(user.location, Location, 'user\'s location should be a Location object')
        self.assertEqual(user.location.get_point(), (34.003135, -117.7228641),
                         'user\'s location should be at the specified coordinates')

        user_list = api.users()
        self.assertEqual(len(user_list), 5, 'users endpoint should return five users')
        for user in user_list:
            self.assertIsInstance(user, User, 'users endpoint should return an list of User objects')
            self.assertIsInstance(user.location, Location, 'users endpoint should return users with Location objects')
        self.assertEqual(user_list[0].id, 1, 'first use ID should be one')
        self.assertEqual(user_list[1].last_name, 'Wyndam-Pryce', 'second user name should be Wyndam-Pryce')
        self.assertEqual(user_list[2].email, 'bhalgarth1@timesonline.co.uk',
                         'third user email should be bhalgarth1@timesonline.co.uk')
        self.assertTrue(user_list[3].location.has_points(), 'fourth user should have a valid location')
        self.assertFalse(user_list[4].location.has_points(), 'fifth user should have a null location')

        city_user_list = api.city_users('Kax')
        self.assertEqual(len(city_user_list), 2, 'city_user endpoint should return two users')
        for user in city_user_list:
            self.assertIsInstance(user, User, 'city_users endpoint should return an list of User objects')
            self.assertIsInstance(user.location, Location,
                                  'city_users endpoint should return users with Location objects')
        self.assertEqual(city_user_list[0].id, 1, 'first user ID should be one')
        self.assertEqual(city_user_list[1].id, 854, 'second user ID should be 854')

