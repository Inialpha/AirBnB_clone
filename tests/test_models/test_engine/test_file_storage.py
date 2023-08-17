#!/usr/bin/python3
"""module for testing storage"""

import unittest
import json
from models.user import User
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models
import os


class TestFileStorage(unittest.TestCase):
    """Test Class for FileStorage that Tests all the method like
        new_storage
        reload method etc
    """

    def setUp(self):
        """ setting up the storage file in init """
        self.storage = FileStorage()
        self.storage.reload()
        self.my_model = BaseModel()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_file_path(self):
        """test for the __file_path attribute"""
        with self.assertRaises(AttributeError):
            return self.storage.__file_path

    def test_object(self):
        """test private class instance __object"""
        with self.assertRaises(AttributeError):
            return self.storage.__object

    def test_all_empty_storage(self):
        """ a method that test all storage functionality """
        all_objs = models.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertFalse(os.path.isfile('file.json'))

    def test_new_storage(self):
        """ a method that test new storage functionality """
        key = self.my_model.id
        stored_obj = self.storage.all()
        model = stored_obj.get(type(self.my_model).__name__ + '.' + key)
        self.assertIsNotNone(model)
        self.assertEqual(model, self.my_model)
        self.assertTrue(type(model), type(self.my_model))

    def test_save_to_storage(self):
        """ a method that test if it's saved to storage """
        self.my_model.save()
        with open('file.json', 'r') as file:
            file_content = file.read()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertIsNotNone(self.my_model)
        self.assertIn(self.check_json_file(file_content), [True, False])

    def check_json_file(self, content):
        """ check if the content of a file is json """
        try:
            json.loads(content)
            return True
        except json.JSONDecodeError:
            return False

    def test_reload(self):
        """a method that test reload functionality """
        objs = self.storage.all()
        for obj in objs.keys():
            inst = objs[obj]
            inst.save()
            self.assertIsNotNone(obj)
            self.assertTrue(inst, dict)
            self.assertTrue(os.path.isfile('file.json'))
            self.assertIsNotNone(str(inst))


if __name__ == '__main__':
    unittest.main()
