#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """Getter attribute that returns list of City instances"""
        cities_instances = []
        storage = models.storage.all()
        for key, value in storage.items():
            if isinstance(value, City) and value.state_id == self.id:
            #if (value.get("__class__") == "City" and
                    #value.get("state") == self.id):
                cities_instances.append(value)
        return cities_instances
