#!/usr/bin/python3
""" a module that test Review class """


import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing Review class for the added functionalities
        Check for class attributes and other methods
    """

    def setUp(self):
        self.my_user = User()
        self.my_review = Review()
        self.my_place = Place()

    def test_review(self):
        """ Testing class attribute data types """
        self.assertTrue(type(self.my_review.place_id), str)
        self.assertTrue(type(self.my_review.user_id), str)
        self.assertTrue(type(self.my_review.text), str)

    def test_none(self):
        """ Testing for None """
        self.my_review.place_id = None
        self.my_review.user_id = None
        self.my_review.text = None
        self.assertEqual(self.my_review.text, None)
        self.assertEqual(self.my_review.user_id, None)
        self.assertEqual(self.my_review.text, None)

    def test_review_attribute(self):
        """ Testing class attribute if has attribute """
        self.my_review.place_id = self.my_place.id
        self.my_review.user_id = self.my_user.id
        self.my_review.text = 'A beautiful house'
        self.assertEqual(self.my_review.place_id, self.my_place.id)
        self.assertEqual(self.my_review.user_id, self.my_user.id)
        self.assertEqual(self.my_review.text, 'A beautiful house')
        self.assertIsNotNone(self.my_review.text)

    def test_amenity_inherit_base_class(self):
        """ Testing User Class to know if it inherit base class """
        self.assertTrue(isinstance(self.my_review, BaseModel))
        self.assertTrue(isinstance(self.my_place, BaseModel))


if __name__ == '__main__':
    unittest.main()
