#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models import storage


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place")

    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False, backref="place")

    @property
    def reviews(self):
        """ Getter attribute for reviews of places """
        obj = storage.all()
        reviews = []
        for key, value in obj.items():
            if "Review" in key and value.place_id == self.id:
                reviews.append(value)
        return reviews

    @property
    def amenities(self):
        """ Getter attribute for amenities of places """
        obj = storage.all()
        amenities = []
        for key, value in obj.items():
            if "Amenity" in key and value.place_id == self.id:
                amenities.append(value)
        return amenities
