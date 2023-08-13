#!/usr/bin/python3
"""module for the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel class
        Public Class Attribute:
        state_id: stores the location in which the city is located in the
            state identify by an ID
        name: sotres the name of the city
    """

    state_id = ""
    name = ""
