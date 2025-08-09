#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os
from dotenv import load_dotenv

load_dotenv()

class State(BaseModel, Base):
    """ The state class, contains state ID and name """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'DBStorage':
        cities = relationship('City', backref='state',
                          cascade="add, delete, delete-orphan")
    else:
        @property
        def cities(self):
            state_city = []
            all_cities = models.storage.all(City)

            for city in all_cities.values():
                if city.state_id == self.id():
                    state_city.append(city)

            return state_city
