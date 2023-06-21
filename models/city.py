#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Represents the City Class

    Attributes:
        __tablename__ (str): MySQL table name.
        name (sqlalchemy String): name of the city.
        state_id (sqlalchemy String): id of city.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
