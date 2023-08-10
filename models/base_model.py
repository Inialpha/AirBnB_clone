#!/usr/bin/python3
"""This is the base module which contain
the BaseModel class inherited by all other major class in the project"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class serve as a base class for all class"""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if len(kwargs) > 0:
            self.__recreate_method(**kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints the representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """update the updated_at instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return the dictionary representation of an object"""

        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return my_dict

    def __recreate_method(self, **kwargs):
        """ a private method that recreates an instance with
            dict representation
        """
        for attr, value in kwargs.items():
            if attr == 'updated_at' or attr == 'created_at':
                setattr(self, attr, datetime.fromisoformat(value))
            elif attr == '__class__':
                pass
            else:
                setattr(self, attr, value)
