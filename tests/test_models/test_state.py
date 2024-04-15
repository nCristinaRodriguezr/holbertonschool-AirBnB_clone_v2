#!/usr/bin/python3
""" State unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ State unittest tests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def setUp(self):
        """Executed before each test"""
        self.state = State()

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Verify attributes are present"""
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertTrue(hasattr(self.state, 'cities'))

    def test_name_type(self):
        """Verify name attribute type"""
        self.assertIsInstance(self.state.name, str)

    def test_cities_relationship(self):
        """Verify cities relationship"""
        city = City(state_id=self.state.id)
        self.assertIn(city, self.state.cities)

    def test_cities_property(self):
        """Verify cities property"""
        city = City(state_id=self.state.id)
        self.assertIn(city, self.state.cities)

if __name__ == '__main__':
    unittest.main()
