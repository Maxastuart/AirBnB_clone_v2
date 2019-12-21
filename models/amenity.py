#!/usr/bin/python3
"""This is the amenity class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import (relationship, Table, MetaData,
                        Column, String, Integer, Float, ForeignKey)
import os


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place',
                                   secondary='place_amenity',
                                   back_populates='amenities')
