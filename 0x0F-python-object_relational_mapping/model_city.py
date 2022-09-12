#!/usr/bin/python3
"""
A python file that contains the class definition of a
City and an instance Base = declarative_base()
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """City class representing states table in db """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", backref="cities")

    def __init__(self, name):
        """Initialize the City class """
        self.name = name
