from haversine import haversine, Unit


class User:

    def __init__(self, user_spec=None):

        if user_spec is None:
            user_spec = {}
        self.id = user_spec.get('id')
        self.first_name = user_spec.get('first_name')
        self.last_name = user_spec.get('last_name')
        self.email = user_spec.get('email')
        self.ip_address = user_spec.get('ip_address')
        self.city = user_spec.get('city')
        if 'latitude' in user_spec and 'longitude' in user_spec:
            self.location = Location(
                float(user_spec['latitude']),
                float(user_spec['longitude'])
            )
        else:
            self.location = Location()

    def to_dict(self):
        return\
            {
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'ip_address': self.ip_address,
                'city': self.city,
                'latitude': self.location.latitude,
                'longitude': self.location.longitude,
            }


class Location:

    def __init__(self, latitude=None, longitude=None):
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError) as e:
            self.latitude = None
            self.longitude = None

    def get_point(self):
        return self.latitude, self.longitude

    def has_points(self):
        return self.latitude is not None and self.longitude is not None

    def distance_to(self, other_location, unit=Unit.MILES):
        if self.has_points() and other_location.has_points():
            return haversine(
                self.get_point(),
                other_location.get_point(),
                unit=unit
            )
        else:
            return None


class City:

    def __init__(self, name, latitude, longitude):
        self.name = name,
        self.location = Location(latitude, longitude)
