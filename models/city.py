#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    City class represents a city.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        name (str): The name of the city.
        state_id (str): The ID of the state to which the city belongs.
        places (relationship): Relationship to the Place class.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", cascade="all, delete", backref="cities")

