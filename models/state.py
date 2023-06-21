#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents the State Class

    Attributes:
        __tablename__ (str): MySQL table name.
        name (sqlalchemy String): name of the State.
        cities (sqlalchemy relationship): State-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
