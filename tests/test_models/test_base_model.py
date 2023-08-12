#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

""" a test file that checks all methods """


class TestBase(unittest.TestCase):
    """ A test for the base class
        Attributes:
            public_attributes: tested
        Methods:
            to_dict: tested to dictionary method
    """
    my_base = BaseModel()
    my_base.name = "First Model"
    my_base.my_number = 89

    def test_public_attribute(self):
        """ a method that test attribute """
        self.assertIsNotNone(self.my_base.id)
        self.assertEqual(self.my_base.name, 'First Model')
        self.assertEqual(self.my_base.my_number, 89)
        self.assertIsInstance(self.my_base.created_at, datetime)
        self.assertFalse(self.my_base.created_at is self.my_base.updated_at)

    def test_recreate_method(self):
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

    def test_to_dictionary(self):
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
