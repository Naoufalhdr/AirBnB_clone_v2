#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class represents amenities available in a place.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        name (str): The name of the amenity.
        place_amenities (relationship): Relationship to the Place class.
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity", overlaps="amenities")
