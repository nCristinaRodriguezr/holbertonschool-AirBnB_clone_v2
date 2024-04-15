#!/usr/bin/python3
""" Review unittest tests """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ Review unittest tests """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)

     def setUp(self):
        """Executed before each test"""
        self.review = Review()

    def test_instance(self):
        """Verify if it instantiates correctly"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Verify attributes are present"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_place_id_type(self):
        """Verify place_id attribute type"""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_type(self):
        """Verify user_id attribute type"""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_type(self):
        """Verify text attribute type"""
        self.assertIsInstance(self.review.text, str)

if __name__ == '__main__':
    unittest.main()