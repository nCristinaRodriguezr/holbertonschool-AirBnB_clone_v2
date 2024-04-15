#!/usr/bin/python3
""" User unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ User unittest tests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)

    def setUp(self):
        """Runs before each test"""
        self.user = User()

    def test_instance(self):
        """Check if it is instantiated correctly"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Verify that the attributes are present"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attributes_types(self):
        """Verify that attributes have the correct types"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_relationships(self):
        """Check class relationships"""
        self.assertTrue(hasattr(self.user, 'places'))
        self.assertTrue(hasattr(self.user, 'reviews'))

    def test_relationships_type(self):
        """Check relationship types"""
        from models.place import Place
        from models.review import Review
        self.assertIsInstance(self.user.places, list)
        self.assertIsInstance(self.user.reviews, list)
        self.assertTrue(all(isinstance(place, Place) for place in self.user.places))
        self.assertTrue(all(isinstance(review, Review) for review in self.user.reviews))

    def test_relationships_backref(self):
        """Check the relationships backref"""
        from models.place import Place
        from models.review import Review
        place = Place(user=self.user)
        review = Review(user=self.user)
        self.assertIn(place, self.user.places)
        self.assertIn(review, self.user.reviews)

    def test_relationships_cascade_delete(self):
        """Check the elimination cascade"""
        from models.place import Place
        from models.review import Review
        place = Place(user=self.user)
        review = Review(user=self.user)
        self.assertIn(place, self.user.places)
        self.assertIn(review, self.user.reviews)
        self.user.delete()
        self.assertNotIn(place, self.user.places)
        self.assertNotIn(review, self.user.reviews)

if __name__ == '__main__':
    unittest.main()
