#!/usr/bin/python3
"""module for the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place Class that inherits the Base Model
        Public method:
            city_id: a class attribute that stores city id
            user_id: a class attribute that sotres user id
            name: a class attribute that stores name of place
            description: a class attribute that stores description
            number_rooms: a class attribute that stores number of rooms
            number_bathrooms: a class attribute that stores number of bathrms
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
