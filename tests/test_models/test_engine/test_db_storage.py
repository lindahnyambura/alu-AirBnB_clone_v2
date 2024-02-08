#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these test if the storage is not db
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not fs")
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.storage

    def test_user(self):
        """ Tests user """
        user = User(name="Abissa")
        user.save()
        self.assertTrue(user.id in self.storage.all())
        self.assertEqual(user.name, "Abissa")

    def test_city(self):
        """ test user """
        city = City(name="Fremont")
        state = State()
        city.state_id ="<new state ID>" name="Fremont"
        city.save()
        self.assertTrue(city.id in self.storage.all())
        self.assertEqual(city.name, "Fremont")

    def test_state(self):
        """ test state"""
        state = State(name="California", city_id="Fremont")
        state.save()
        self.assertTrue(state.id in self.storage.all())
        self.assertEqual(state.city_id,"Fremont")
        self.assertEqual(state.name, "California")

    def test_place(self):
        """ test place """
        place = Place(name="Palace", number_rooms=4)
        place.save()
        self.assertTrue(place.id in self.storage.all())
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "Palace")

    def test_amenity(self):
        """ test amenity """
        amenity = Amenity(name="Startlink")
        amenity.save()
        self.assertTrue(amenity.id in self.storage.all())
        self.assertTrue(amenity.name, "Startlink")

    def test_review(self):
        """ test review """
        review = Review(text="no comment")
        review.save()
        self.assertTrue(review.id in self.storage.all())
        self.assertEqual(review.text, "no comment")
    
    def test_create_state_california(self):
        """ test creation of a State with name 'California' """
        state = State(name="California")
        state.save()
        self.assertTrue(state.id in self.storage.all())
        self.assertEqual(state.name, "California")
