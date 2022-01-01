from haversine import haversine, Unit


class User:
    """Encapsulates a user as returned by the API. The user's location is held as a Location object"""
    def __init__(self, user_spec=None):
        """Initialises the user from the supplied JSON spec"""
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
        """Returns the user as a Python dictionary for easy conversion to JSON"""
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
    """Encapsulates a location as a latitude/longitude pair"""
    def __init__(self, latitude=None, longitude=None):
        """Accepts a latitude and longitude and initialises them internally with (some) type checking"""
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError) as e:
            self.latitude = None
            self.longitude = None

    def get_point(self):
        """Returns the latitude and longitude as a tuple. Returns (None, None) if the object hasn't been initialised"""
        return self.latitude, self.longitude

    def has_points(self):
        """Checks whether the Location object has a valid latitude and longitude. Returns a boolean."""
        return self.latitude is not None and self.longitude is not None

    def distance_to(self, other_location, unit=Unit.MILES):
        """
        Calculates the haversine-derived distance between two locations
        :param other_location: a Location object to which the distance will be measured
        :param unit: the units in which the distance will be returned. Defaults to miles.
        :return: distance in the given units, or None if either location is invalid
        """
        if self.has_points() and other_location.has_points():
            return haversine(
                self.get_point(),
                other_location.get_point(),
                unit=unit
            )
        else:
            return None


class City:
    """Encapsulates a city, with a name and a Location object representing its centre"""
    def __init__(self, name, latitude, longitude):
        self.name = name,
        self.location = Location(latitude, longitude)
