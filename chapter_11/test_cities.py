import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """tests for city_functions.py"""

    def test_city_country(self):
        """do cities like 'Santiago, Chile' work?"""
        city = city_country('santiago', 'chile')
        self.assertEqual(city, 'Santiago, Chile')

    def test_city_country_population(self):
        """does a format like 'Santiago, Chile - population: 5000000' work?"""
        city = city_country('santiago', 'chile', 5000000)
        self.assertEqual(city, 'Santiago, Chile - Population: 5000000')

unittest.main()