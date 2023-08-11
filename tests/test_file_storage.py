#!/usr/bin/python3

import unittest, os, json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Test Class for FileStorage """
    
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89

    def test_all_empty_storage(self):
        """ a method that test all storage functionality """
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertIsNotNone(obj)
        self.assertTrue(os.path.isfile('file.json'))
    
    def test_new_storage(self):
        """ a method that test new storage functionality """
        key = self.my_model.id
        stored_obj = storage.all()
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

    def test_reload_from_file(self):
        """ a method that test reload functionality """
        objs = storage.all()
        for obj in objs.keys():
            inst = objs[obj]
            self.assertIsNotNone(obj)
            self.assertTrue(inst, dict)
        self.assertTrue(os.path.isfile('file.json'))


if __name__ == '__main__':
    unittest.main()
