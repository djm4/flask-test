from flask import current_app
from .bpdts_test_app_api import BPDTSTestAppAPI
from .user import User


class APIWrapper:

    def __init__(self):
        self.api = (BPDTSTestAppAPI(current_app.config['BPDTS_API_URL']))

    def instructions(self):
        return self.api.instructions()

    def user(self, id):
        user = self.api.user(id)
        return User(user)

    def users(self):
        user_list = self.api.users()
        return [User(user) for user in user_list]

    def city_users(self, city):
        city_user_list = self.api.city_users(city)
        return [User(user) for user in city_user_list]