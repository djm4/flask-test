import unittest
from app.user import Location


class LocationTestCase(unittest.TestCase):

    def test_location(self):
        location_1 = Location(0, 0)
        location_2 = Location(0, 1)
        location_3 = Location(50, 0)
        location_4 = Location(51, 0)
        self.assertEqual(location_2.latitude, 0)
        self.assertEqual(location_2.longitude, 1)
        self.assertAlmostEqual(location_1.distance_to(location_2), 69.093, 3)
        self.assertAlmostEqual(location_3.distance_to(location_4), 69.093, 3)
        self.assertAlmostEqual(location_1.distance_to(location_2), location_2.distance_to(location_1))
        self.assertAlmostEqual(location_1.distance_to(location_2), location_3.distance_to(location_4))


if __name__ == '__main__':
    unittest.main()
