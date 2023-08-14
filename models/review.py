#!/usr/bin/python3
"""module for the Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits the BaseModel
        Public attributes:
            place_id: a attribute that stores the place id
            user_id: a attribute that store user_id
            text: an attribute that stores review of clients
    """
    place_id = ""
    user_id = ""
    text = ""
