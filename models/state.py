#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models
import os
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                cascade='all, delete', backref='states')
    else:
        @property
        def cities(self):
            """returns the list of city instances"""
            c_inst = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    c_inst.append(city)
            return c_inst
