#!/usr/bin/python3
"""module for user unittest"""

import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    """ testing class attributes """

    def setUp(self):
        """the setup method"""
        self.my_user = User()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """ Testing class attribute data types """
        self.assertTrue(isinstance(self.my_user, User))
        self.assertTrue(isinstance(self.my_user, BaseModel))

    def test_id(self):
        """test user id"""
        self.assertIsNotNone(self.my_user.id)
        self.assertIsInstance(self.my_user.id, str)

    def test_created_at(self):
        """test the created_at instance attribute"""
        self.assertIsNotNone(self.my_user.created_at)
        self.assertIsInstance(self.my_user.created_at, datetime)

    def test_updated_at(self):
        """test the updated_at attribute"""
        self.assertIsNotNone(self.my_user.updated_at)
        self.assertIsInstance(self.my_user.updated_at, datetime)

    def test_to_dict(self):
        """test the to_duct method"""
        my_dict = self.my_user.to_dict()
        self.assertIsInstance(my_dict, dict)

    def test_save(self):
        """test the save method"""
        self.my_user.save()
        self.assertTrue(os.path.exists("file.json"))

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

        """ Testing check if dictionary was create when save was called """
        self.my_user.save()
        self.assertIsNotNone(self.my_user.created_at)
        self.assertTrue(type(self.my_user), dict)


if __name__ == '__main__':
    unittest.main()
