#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

""" a test file that checks all methods """


class TestBase(unittest.TestCase):
    """ a test for the base class """

    def test_recreate_method(self):
        """ a method that test if a dictionary was supplied """
        my_base = BaseModel()
        my_base.name = "First Model"
        my_base.my_number = 89
        my_json_base = my_base.to_dict()
        new_base = BaseModel(**my_json_base)
        empty_json = {}
        base_empty = BaseModel(**empty_json)
        self.assertIsNotNone(base_empty.id)
        self.assertEqual(my_base.id, new_base.id)
        self.assertEqual(type(new_base.created_at), type(my_base.created_at))
        self.assertFalse(my_base is new_base)
        self.assertIsNotNone(new_base.id)


if __name__ == '__main__':
    unittest.main()
