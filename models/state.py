#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.city import City
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
            String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                'City'
                cascade='all, delete, delete-orphan'
                backref='state')
    else:
        @property
        def cities(self):
            """ Return cities in State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state

