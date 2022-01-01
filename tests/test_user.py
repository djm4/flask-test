import unittest
from app.user import User


class UserCase(unittest.TestCase):
    """Performs tests relating to the User object"""
    def test_user(self):
        user = User(
            {
                  "id": 1,
                  "first_name": "Maurise",
                  "last_name": "Shieldon",
                  "email": "mshieldon0@squidoo.com",
                  "ip_address": "192.57.232.111",
                  "latitude": 34.003135,
                  "longitude": -117.7228641,
                  "city": "Kax"
            })
        self.assertEqual(user.id, 1, 'User object ID should be 1')
        self.assertEqual(user.first_name, 'Maurise', 'User object first name should be Maurise')
        self.assertEqual(user.last_name, 'Shieldon', 'User object last name should be Shieldon')
        self.assertEqual(user.email, 'mshieldon0@squidoo.com', 'User object email should be mshieldon0@squidoo.com')
        self.assertEqual(user.ip_address, '192.57.232.111', 'User object IP address should be 192.57.232.111')
        self.assertEqual(user.city, 'Kax', 'User object city should be Kax')
        self.assertEqual(user.location.get_point(), (34.003135, -117.7228641),
                         'User object location should be (34.003135, -117.7228641)')


if __name__ == '__main__':
    unittest.main()
