from haversine import Unit
from .user import City

units = {
    'miles': Unit.MILES,
    'nautical_miles': Unit.NAUTICAL_MILES,
    'kilometers': Unit.KILOMETERS,
    'meters': Unit.METERS,
    'feet': Unit.FEET,
    'inches': Unit.INCHES,
    'radians': Unit.RADIANS,
    'degrees': Unit.DEGREES
}

cities = {
    'London': City('London', 51.507351, -0.127670),   # Original Charing Cross site
    'Kax': City('Kax', 34.055678, -118.243405)        # Arbitrary near LA for testing
}
