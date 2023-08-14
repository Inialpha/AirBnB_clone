#!/usr/bin/python3
""" test file for city class """


import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestCity(unittest.TestCase):
    """ testing child class """
    my_user = User()
    my_city = City()
    my_state = State()
    my_amenity = Amenity()
    my_review = Review()
    my_place = Place()

    def test_child_class_type(self):
        """ Testing class attribute data types """
        self.assertTrue(type(self.my_state.name), str)
        self.assertTrue(type(self.my_city.id), str)
        self.assertTrue(type(self.my_city.name), str)
        self.assertTrue(type(self.my_amenity.name), str)
        self.assertTrue(type(self.my_review.place_id), str)
        self.assertTrue(type(self.my_review.user_id), str)
        self.assertTrue(type(self.my_review.text), str)

    def test_place_type(self):
        """ Testing Place class attributes type """
        self.assertTrue(type(self.my_place.city_id), str)
        self.assertTrue(type(self.my_place.user_id), str)
        self.assertTrue(type(self.my_place.name), str)
        self.assertTrue(type(self.my_place.description), str)
        self.assertTrue(type(self.my_place.number_rooms), int)
        self.assertTrue(type(self.my_place.number_bathrooms), int)
        self.assertTrue(type(self.my_place.max_guest), int)
        self.assertTrue(type(self.my_place.price_by_night), int)
        self.assertTrue(type(self.my_place.latitude), float)
        self.assertTrue(type(self.my_place.longitude), float)
        self.assertTrue(type(self.my_place.amenity_ids), list)

    def test_child_class_attribute(self):
        """ Testing class attribute if has attribute """
        self.my_state.name = 'Abuja'
        self.my_city.id = self.my_state.id
        self.my_city.name = 'Maitama'
        self.my_amenity.name = 'Power Supply'
        self.my_review.place_id = self.my_place.id
        self.my_review.user_id = self.my_user.id
        self.my_review.text = 'A beautiful house'

        self.assertEqual(self.my_state.name, 'Abuja')
        self.assertEqual(self.my_city.id, self.my_state.id)
        self.assertEqual(self.my_city.name, 'Maitama')
        self.assertEqual(self.my_amenity.name, 'Power Supply')
        self.assertEqual(self.my_review.place_id, self.my_place.id)
        self.assertEqual(self.my_review.user_id, self.my_user.id)
        self.assertEqual(self.my_review.text, 'A beautiful house')
        self.assertIsNotNone(self.my_review.text)

    def test_user_inherits_base_class(self):
        """ Testing User Class to know if it inherit base class """
        self.assertTrue(isinstance(self.my_state, BaseModel))
        self.assertTrue(isinstance(self.my_city, BaseModel))
        self.assertTrue(isinstance(self.my_amenity, BaseModel))
        self.assertTrue(isinstance(self.my_review, BaseModel))
        self.assertTrue(isinstance(self.my_place, BaseModel))


if __name__ == '__main__':
    unittest.main()
