#!/usr/bin/python3
"""module for FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
import os


class FileStorage:
    """this class serializes instances to
    a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "."
        key += str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        j_dict = {}
        for key in self.__objects:
            j_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(j_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
