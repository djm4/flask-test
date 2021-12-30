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
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_users_near_city(self):
        response = self.client.get('/v1/users_in_or_near/Kax/miles/50')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(json_response), 3)
        id_list = [x['id'] for x in json_response.values()]
        id_list.sort()
        self.assertEqual(id_list, [1, 2, 854])

    def test_api_wrapper(self):
        api = APIWrapper()
        self.assertIn('todo', api.instructions())
        user = api.user(1)
        self.assertIsInstance(user, User)
        self.assertEqual(user.first_name, 'Maurise')
        self.assertIsInstance(user.location, Location)
        self.assertEqual(user.location.get_point(), (34.003135, -117.7228641))

        user_list = api.users()
        self.assertEqual(len(user_list), 5)
        for user in user_list:
            self.assertIsInstance(user, User)
            self.assertIsInstance(user.location, Location)
        self.assertEqual(user_list[0].id, 1)
        self.assertEqual(user_list[1].last_name, 'Wyndam-Pryce')
        self.assertEqual(user_list[2].email, 'bhalgarth1@timesonline.co.uk')
        self.assertTrue(user_list[3].location.has_points())
        self.assertFalse(user_list[4].location.has_points())

        city_user_list = api.city_users('Kax')
        self.assertEqual(len(city_user_list), 2)
        for user in city_user_list:
            self.assertIsInstance(user, User)
            self.assertIsInstance(user.location, Location)
        self.assertEqual(city_user_list[0].id, 1)
        self.assertEqual(city_user_list[1].id, 854)

