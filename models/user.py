#!/usr/bin/python

""" a module that create a user profile """

from .base_model import BaseModel


class User(BaseModel):
    """ a class that inherits the properties of base class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
