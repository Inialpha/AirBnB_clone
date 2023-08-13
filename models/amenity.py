#!/usr/bin/python3
"""module for the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits the methods in base model
        Public method:
            name: store the name of the amenity of the house
    """

    name = ""
