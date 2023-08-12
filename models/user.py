#!/usr/bin/python

""" a module that create a user profile """

from .base_model import BaseModel


class User(BaseModel):
    """ a class that inherits the properties of base class
        Public attributes:
            email: an attributes that stores email
            password: an attributes that stores password
            first_name: an attributes that stores first_name
            last_name: an attributes that store last_name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
