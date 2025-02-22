#!/usr/bin/python3
"""Place Module for HBNB project"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
from models.user import User

# Constants
PLACES_TABLE_NAME = "places"

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey(f'{PLACES_TABLE_NAME}.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = PLACES_TABLE_NAME
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship("Review",
                               backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place_amenity", viewonly=False)

    else:
        city_id = None
        user_id = None
        name = None
        description = None
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initializes Place"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """Getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Getter attribute returns the list of Amenity instances"""
            from models.amenity import Amenity
            amenity_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

