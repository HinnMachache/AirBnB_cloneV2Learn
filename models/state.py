#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ The state class, contains state ID and name """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade="add, delete, delete-orphan")
    
    @property
    def cities(self):
        return City
    
