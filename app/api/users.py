from flask import jsonify
from . import api
from .errors import bad_request
from ..api_wrappper import APIWrapper
from ..constants import cities, units


@api.route('/users_in_or_near/<city>/<unit>/<distance>')
def get_users_in_or_near(city, unit, distance):
    if unit in units:
        unit = units[unit]
    else:
        permitted_units = ', '.join(units.keys())
        return bad_request(f'Unit not recognised: {unit}. Permitted units: {permitted_units}')
    try:
        distance = float(distance)
    except (ValueError, TypeError) as e:
        return bad_request(f'{distance} is not convertable to a float')
    if city not in cities:
        return bad_request(f'The city {city} was not recognised')
    user_list = {}
    source_api = APIWrapper()
    users_near_city = source_api.city_users(city)
    for user in users_near_city:
        user_list[user.id] = user.to_dict()
    all_users = source_api.users()
    if city in cities:
        target_city = cities[city]
        for user in all_users:
            separation = user.location.distance_to(target_city.location, unit)
            if separation is not None and separation <= distance:
                user_list[user.id] = user.to_dict()

    return jsonify(user_list)
