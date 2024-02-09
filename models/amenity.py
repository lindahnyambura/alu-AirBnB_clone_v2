#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenity = Table(
                            "place_amenity", Base.metadata,
                            Column('place_id',
                                   String(60),
                                   ForeignKey('places.id'),
                                   primary_key=True,
                                   nullable=False),
                            Column('amenity_id',
                                   String(60),
                                   ForeignKey('amenities.id'),
                                   primary_key=True,
                                   nullable=False))
