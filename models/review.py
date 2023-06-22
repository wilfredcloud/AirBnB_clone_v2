#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review class.
    Attributes:
        __tablename__ (str): MySQL table to store Reviews.
        text (sqlalchemy String):  review description.
        place_id (sqlalchemy String): review's place id.
        user_id (sqlalchemy String): review's user id.
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
