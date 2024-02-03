#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel, Base):
    """defines the table for amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities=
