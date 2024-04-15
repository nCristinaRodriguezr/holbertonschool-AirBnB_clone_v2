#!/usr/bin/python3
""" City unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ City unittest tests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def setUp(self):
        """Executed before each test"""
        self.city = City()

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Verify attributes are present"""
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'places'))

    def test_name_type(self):
        """Verify name attribute type"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id_type(self):
        """Verify state_id attribute type"""
        self.assertIsInstance(self.city.state_id, str)

    def test_places_relationship(self):
        """Verify places relationship"""
        place = Place(city_id=self.city.id)
        self.assertIn(place, self.city.places)

if __name__ == '__main__':
    unittest.main()