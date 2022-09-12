#!/usr/bin/python3
"""
A python file that contains the class definition of a
State and an instance Base = declarative_base()
"""

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    """State class representing states table in db """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="states")

    def __init__(self, name):
        """Initialize the State class """
        self.name = name
