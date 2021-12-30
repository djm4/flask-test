import unittest
from app.user import User


class UserCase(unittest.TestCase):
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
        self.assertEqual(user.id, 1)
        self.assertEqual(user.first_name, 'Maurise')
        self.assertEqual(user.last_name, 'Shieldon')
        self.assertEqual(user.email, 'mshieldon0@squidoo.com')
        self.assertEqual(user.ip_address, '192.57.232.111')
        self.assertEqual(user.city, 'Kax')
        self.assertEqual(user.location.get_point(), (34.003135, -117.7228641))


if __name__ == '__main__':
    unittest.main()
