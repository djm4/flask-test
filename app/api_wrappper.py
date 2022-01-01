from flask import current_app
from .bpdts_test_app_api import BPDTSTestAppAPI
from .user import User


class APIWrapper:
    """
    Wrapper for the BPDTS test API to create objects.

    Probably excessive for this exercise, as the BPDTSTestAppAPI class could
    directly return objects, but gives an extra level of abstraction to make
    the API more extensible.
    """
    def __init__(self):
        """Initialises the BPDTS test API with the appropriate parameter (mock/live)"""
        self.api = (BPDTSTestAppAPI(current_app.config['BPDTS_API_URL']))

    def instructions(self):
        """Returns instructions. This is a simple JSON pass-through"""
        return self.api.instructions()

    def user(self, id):
        """Accepts an integer ID and returns a User object with that ID"""
        user = self.api.user(id)
        return User(user)

    def users(self):
        """Returns an array of users as User objects"""
        user_list = self.api.users()
        return [User(user) for user in user_list]

    def city_users(self, city):
        """Accepts a city and returns an array of users in the city as User objects"""
        city_user_list = self.api.city_users(city)
        return [User(user) for user in city_user_list]