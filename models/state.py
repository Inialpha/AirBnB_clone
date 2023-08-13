#!/usr/bin/python3
"""module for the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ State class that inherits the BaseModel
        Public attributes:
            name: a public attributes that stores name of state
    """

    name = ""
