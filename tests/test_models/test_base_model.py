#!/usr/bin/python3
"""a test module for the base models that checks all methods in the class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import os


class TestBase(unittest.TestCase):
    """ A test for the base class
        Attributes:
            public_attributes: tested
        Methods:
            to_dict: tested to dictionary method
    """
    def setUp(self):
        """setup method"""
        self.my_base = BaseModel()
        self.my_base.name = "First Model"
        self.my_base.my_number = 89
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init(self):
        """check if is instance"""
        self.assertTrue(isinstance(self.my_base, BaseModel))

    def test_id(self):
        """test for id"""
        self.assertIsNotNone(self.my_base.id)
        self.assertTrue(isinstance(self.my_base.id, str))

    def test_created_at(self):
        """test created_at"""
        self.assertIsNotNone(self.my_base.created_at)
        self.assertIsInstance(self.my_base.created_at, datetime)

    def test_updated_at(self):
        """test updated_at"""
        self.assertIsNotNone(self.my_base.updated_at)
        self.assertIsInstance(self.my_base.updated_at, datetime)

    def test_public_attribute(self):
        """ a method that test attribute """
        self.assertEqual(self.my_base.name, 'First Model')
        self.assertEqual(self.my_base.my_number, 89)
        self.assertFalse(self.my_base.created_at is self.my_base.updated_at)

    def test_save(self):
        """test the save method"""
        self.my_base.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_str_(self):
        """test the str method"""
        my_str = "[{}] ({}) {}".format(self.my_base.__class__.__name__,
                                       self.my_base.id, self.my_base.__dict__)
        self.assertEqual(str(self.my_base), my_str)

    def test_kwargs_method(self):
        """ a method that test if a dictionary was supplied """
        my_json_base = self.my_base.to_dict()
        new_base = BaseModel(**my_json_base)
        empty_json = {}
        base_empty = BaseModel(**empty_json)
        self.assertIsNotNone(base_empty.id)
        self.assertEqual(self.my_base.id, new_base.id)
        self.assertEqual(type(new_base.created_at),
                         type(self.my_base.created_at))
        self.assertFalse(self.my_base is new_base)
        self.assertIsNotNone(new_base.id)

    def test_to_dict(self):
        """ a method that test convertion to dictionary """
        base_dict = self.my_base.to_dict()
        for key, value in base_dict.items():
            if key == 'created_at' or key == 'updated_at':
                self.assertEqual(getattr(self.my_base, key),
                                 datetime.fromisoformat(value))
            elif key == '__class__':
                pass
            else:
                self.assertEqual(getattr(self.my_base, key), value)
        self.assertIsInstance(base_dict, dict)


if __name__ == '__main__':
    unittest.main()
