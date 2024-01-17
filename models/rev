#!/usr/bin/python3
"""Review module for the HBNB project"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey

# Constants
REVIEW_TABLE_NAME = "reviews"
PLACES_ID_REFERENCE = "places.id"
USERS_ID_REFERENCE = "users.id"

class Review(BaseModel, Base):
    """Review class to store review information"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = REVIEW_TABLE_NAME
        place_id = Column(String(60), ForeignKey(PLACES_ID_REFERENCE), nullable=False)
        user_id = Column(String(60), ForeignKey(USERS_ID_REFERENCE), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        place_id = None
        user_id = None
        text = None

    def __init__(self, *args, **kwargs):
        """Initialize review"""
        super().__init__(*args, **kwargs)

