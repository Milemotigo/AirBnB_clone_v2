#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table("place_amenity", Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", cascade='all, delete', backref='place')
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """returns the list of review instances"""
        r_inst = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                r_inst.append(review)
        return r_inst

    @property
    def amenities(self):
        """returns the list of amenity instances"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, amenity):
        """handles append method"""
        if type(amenity) is Amenity and amenity.id not in self.amenity_ids:
            self.amenity_ids.append(amenity.id)
