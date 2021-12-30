from flask import jsonify
from . import api
from ..api_wrappper import APIWrapper
from ..constants import cities, units


@api.route('/users_in_or_near/<city>/<unit>/<distance>')
def get_users_in_or_near(city, unit, distance):
    user_list = {}
    if unit in units:
        unit = units[unit]
    source_api = APIWrapper()
    users_near_city = source_api.city_users(city)
    for user in users_near_city:
        user_list[user.id] = user.to_dict()
    all_users = source_api.users()
    if city in cities:
        target_city = cities[city]
        for user in all_users:
            separation = user.location.distance_to(target_city.location, unit)
            if separation is not None and separation <= float(distance):
                user_list[user.id] = user.to_dict()

    return jsonify(user_list)
