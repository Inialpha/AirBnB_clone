#!/usr/bin/python3
"""module for user unittest"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    """ testing class attributes """

    def setUp(self):
        """the setup method"""
        self.my_user = User()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_class_type(self):
        """ Testing class attribute data types """
        self.assertIsNotNone(self.my_user.id)
        self.assertTrue(type(self.my_user.first_name), str)
        self.assertTrue(type(self.my_user.last_name), str)
        self.assertTrue(type(self.my_user.email), str)
        self.assertTrue(type(self.my_user.password), str)

    def test_user_class_attribute(self):
        """ Testing class attribute if has attribute """
        self.my_user.first_name = 'Betty'
        self.my_user.last_name = 'Bar'
        self.my_user.email = 'airbnb@mail.com'
        self.my_user.password = 'root'
        self.assertEqual(self.my_user.first_name, 'Betty')
        self.assertEqual(self.my_user.last_name, 'Bar')
        self.assertEqual(self.my_user.email, 'airbnb@mail.com')
        self.assertEqual(self.my_user.password, 'root')

    def test_user_inherits_base_class(self):
        """ Testing User Class to know if it inherit base class """
        self.assertTrue(isinstance(self.my_user, BaseModel))
        self.assertFalse(isinstance(self.my_user, FileStorage))

    def test_user_has_save_methods(self):
        """ Testing check if dictionary was create when save was called """
        self.my_user.save()
        self.assertIsNotNone(self.my_user.created_at)
        self.assertTrue(type(self.my_user), dict)


if __name__ == '__main__':
    unittest.main()
