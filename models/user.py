#!/usr/bin/python3
"""This module defines a class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

# Constants
USERS_TABLE_NAME = "users"

class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = USERS_TABLE_NAME
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user", cascade="all, delete")
        reviews = relationship("Review", backref="user", cascade="all, delete")

    else:
        email = None
        password = None
        first_name = None
        last_name = None

    def __init__(self, *args, **kwargs):
        """Initialize user"""
        super().__init__(*args, **kwargs)

