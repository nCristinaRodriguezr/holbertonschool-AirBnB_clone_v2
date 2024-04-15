#!/usr/bin/python3
""" Amenity unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Amenity unittest tests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

     def setUp(self):
        """Executed before each test"""
        self.amenity = Amenity()

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """Verify attributes are present"""
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'place_amenities'))

    def test_name_type(self):
        """Verify name attribute type"""
        self.assertIsInstance(self.amenity.name, str)

    def test_place_amenities_relationship(self):
        """Verify place_amenities relationship"""
        # Assuming you have a Place model
        from models.place import Place
        place = Place()
        self.amenity.place_amenities.append(place)
        self.assertIn(place, self.amenity.place_amenities)

if __name__ == '__main__':
    unittest.main()
