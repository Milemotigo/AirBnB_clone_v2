#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    citites = relationship("City", backref='states')

    @property
    def cities(self):
        """returns the list of city instances"""
        c_inst = []
        for city in models.storage.all('City').values():
            if city.state_id == self.id:
                c_inst.append(city)
        return c_inst
