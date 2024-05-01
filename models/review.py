#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """
    Review class stores review information.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        text (str): The text content of the review.
        place_id (str): The ID of the place associated with the review.
        user_id (str): The ID of the user who wrote the review.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
