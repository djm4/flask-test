import unittest
from app.bpdts_test_app_api import BPDTSTestAppAPI
from app.user import User, Location


class BPDTSTestAppAPITestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.liveAPI = BPDTSTestAppAPI(base_url='https://bpdts-test-app.herokuapp.com')
        self.mockAPI = BPDTSTestAppAPI(base_url='mock')

    def test_instructions(self):
        live_instructions = self.liveAPI.instructions()
        self.assertIn('todo', live_instructions, 'instructions endpoint should have todo as a key')

        mock_instructions = self.mockAPI.instructions()
        self.assertIn('todo', mock_instructions)
        self.assertEqual(mock_instructions['todo'],
                         'Build an API which calls this API, and returns people who are listed as either'
                         + ' living in London, or whose current coordinates are within 50 miles of London.'
                         + ' Push the answer to Github, and send us a link.'
                         , 'instructions mock endpoint should return specific text')

    def test_users(self):
        mock_users = self.mockAPI.users()
        self.assertEqual(len(mock_users), 5, 'users endpoint should return five users')
        first_user = mock_users[0]
        self.assertIn('id', first_user, 'User should have an \'id\' field')
        self.assertIn('first_name', first_user, 'User should have a \'first_name\' field')
        self.assertIn('last_name', first_user, 'User should have a \'last_name\' field')
        self.assertIn('email', first_user, 'User should have an \'email\' field')
        self.assertIn('ip_address', first_user, 'User should have an \'ip_address\' field')
        self.assertIn('latitude', first_user, 'User should have a \'latitude\' field')
        self.assertIn('longitude', first_user, 'User should have a \'longitude\' field')
        self.assertEqual(first_user['id'], 1, 'User ID should be one')
        self.assertEqual(first_user['first_name'], 'Maurise', 'User first name should be Maurise')
        self.assertEqual(first_user['last_name'], 'Shieldon', 'User last name should be Shieldon')
        self.assertEqual(first_user['email'], 'mshieldon0@squidoo.com', 'User email should be mshieldon0@squidoo.com')
        self.assertEqual(first_user['ip_address'], '192.57.232.111', 'User IP address should be 192.57.232.111')
        self.assertEqual(first_user['latitude'], 34.003135, 'User latitude should be 34.003135')
        self.assertEqual(first_user['longitude'], -117.7228641, 'User longitude should be -117.7228641')

        first_user_obj = User(first_user)
        self.assertEqual(first_user_obj.id, 1, 'User object ID should be one')
        self.assertEqual(first_user_obj.first_name, 'Maurise', 'User object first name should be Maurise')
        self.assertEqual(first_user_obj.last_name, 'Shieldon', 'User object last name should be Shieldon')
        self.assertEqual(first_user_obj.email, 'mshieldon0@squidoo.com',
                         'User object email should be mshieldon0@squidoo.com')
        self.assertEqual(first_user_obj.ip_address, '192.57.232.111', 'User object IP address should be 192.57.232.111')
        self.assertIsNone(first_user_obj.city, 'User object should have no city')
        self.assertEqual(first_user_obj.location.latitude, 34.003135, 'User object latitude should be 34.003135')
        self.assertEqual(first_user_obj.location.longitude, -117.7228641,
                         'User object longitude should be -117.7228641')

    def test_user(self):
        mock_user = self.mockAPI.user(1)
        self.assertIn('id', mock_user, 'User should have an \'id\' field')
        self.assertIn('first_name', mock_user, 'User should have a \'first_name\' field')
        self.assertIn('last_name', mock_user, 'User should have a \'last_name\' field')
        self.assertIn('email', mock_user, 'User should have an \'email\' field')
        self.assertIn('ip_address', mock_user, 'User should have an \'ip_address\' field')
        self.assertIn('latitude', mock_user, 'User should have a \'latitude\' field')
        self.assertIn('longitude', mock_user, 'User should have a \'longitude\' field')
        self.assertIn('city', mock_user, 'User should have a \'city\' field')
        self.assertEqual(mock_user['id'], 1, 'User ID should be one')
        self.assertEqual(mock_user['first_name'], 'Maurise', 'User first name should be Maurise')
        self.assertEqual(mock_user['last_name'], 'Shieldon', 'User last name should be Shieldon')
        self.assertEqual(mock_user['email'], 'mshieldon0@squidoo.com', 'User email should be mshieldon0@squidoo.com')
        self.assertEqual(mock_user['ip_address'], '192.57.232.111', 'User IP address should be 192.57.232.111')
        self.assertEqual(mock_user['latitude'], 34.003135, 'User latitude should be 34.003135')
        self.assertEqual(mock_user['longitude'], -117.7228641, 'User longitude should be -117.7228641')
        self.assertEqual(mock_user['city'], 'Kax', 'User city should be Kax')

        mock_user_obj = User(mock_user)
        self.assertEqual(mock_user_obj.id, 1, 'User object ID should be one')
        self.assertEqual(mock_user_obj.first_name, 'Maurise', 'User object first name should be Maurise')
        self.assertEqual(mock_user_obj.last_name, 'Shieldon', 'User object last name should be Shieldon')
        self.assertEqual(mock_user_obj.email, 'mshieldon0@squidoo.com',
                         'User object email should be mshieldon0@squidoo.com')
        self.assertEqual(mock_user_obj.ip_address, '192.57.232.111', 'User object IP address should be 192.57.232.111')
        self.assertEqual(mock_user_obj.city, 'Kax', 'User object city should be Kax')
        self.assertEqual(mock_user_obj.location.latitude, 34.003135, 'User object latitude should be 34.003135')
        self.assertEqual(mock_user_obj.location.longitude, -117.7228641,
                         'User object longitude should be -117.7228641')

        los_angeles_location = Location(34.055426, -118.246759)
        self.assertAlmostEqual(mock_user_obj.location.distance_to(los_angeles_location), 30.2156, 4,
                               'User location should be approximately 30.2156 miles from LA')

    def test_city_users(self):
        mock_users = self.mockAPI.city_users('Kax')
        self.assertEqual(len(mock_users), 2, 'city_users endpoint should return two users')
        first_user = mock_users[0]
        self.assertIn('id', first_user, 'User should have an \'id\' field')
        self.assertIn('first_name', first_user, 'User should have a \'first_name\' field')
        self.assertIn('last_name', first_user, 'User should have a \'last_name\' field')
        self.assertIn('email', first_user, 'User should have an \'email\' field')
        self.assertIn('ip_address', first_user, 'User should have an \'ip_address\' field')
        self.assertIn('latitude', first_user, 'User should have a \'latitude\' field')
        self.assertIn('longitude', first_user, 'User should have a \'longitude\' field')
        self.assertEqual(first_user['id'], 1, 'User ID should be one')
        self.assertEqual(first_user['first_name'], 'Maurise', 'User first name should be Maurise')
        self.assertEqual(first_user['last_name'], 'Shieldon', 'User last name should be Shieldon')
        self.assertEqual(first_user['email'], 'mshieldon0@squidoo.com', 'User email should be mshieldon0@squidoo.com')
        self.assertEqual(first_user['ip_address'], '192.57.232.111', 'User IP address should be 192.57.232.111')
        self.assertEqual(first_user['latitude'], 34.003135, 'User latitude should be 34.003135')
        self.assertEqual(first_user['longitude'], -117.7228641, 'User longitude should be -117.7228641')

        first_user_obj = User(first_user)
        self.assertEqual(first_user_obj.id, 1, 'User object ID should be one')
        self.assertEqual(first_user_obj.first_name, 'Maurise', 'User object first name should be Maurise')
        self.assertEqual(first_user_obj.last_name, 'Shieldon', 'User object last name should be Shieldon')
        self.assertEqual(first_user_obj.email, 'mshieldon0@squidoo.com',
                         'User object email should be mshieldon0@squidoo.com')
        self.assertEqual(first_user_obj.ip_address, '192.57.232.111', 'User object IP address should be 192.57.232.111')
        self.assertIsNone(first_user_obj.city, 'User object should have no city')
        self.assertEqual(first_user_obj.location.latitude, 34.003135, 'User object latitude should be 34.003135')
        self.assertEqual(first_user_obj.location.longitude, -117.7228641,
                         'User object longitude should be -117.7228641')


if __name__ == '__main__':
    unittest.main()
