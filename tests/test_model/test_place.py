#!/usr/bin/python3

from unittest import TestCase
from models.place import Place
from datetime import datetime


class TestPlace(TestCase):
    def setUp(self):
        self.b1 = Place()
        self.b1.created_at = datetime.now()
        self.b1.updated_at = datetime.now()
        self.b2 = Place()

    def test_id(self):
        self.model_test = Place()
        self.assertNotEqual(self.b1.id, self.model_test.id)

    def test_save(self):
        updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(updated_at, self.b1.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Place.{}".format(self.b1.id), file.read())

    def test_to_dict(self):
        new = self.b1.to_dict()
        self.assertEqual(new["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.b1.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.b1.__class__.__name__)

    def test__str__(self):
        className = self.b1.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.b1.id, self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())

    def test_city_id(self):
        self.assertTrue(hasattr(self.b2, "city_id"))
        self.assertEqual(self.b2.city_id, "")

    def test_user_id(self):
        self.assertTrue(hasattr(self.b2, "user_id"))
        self.assertEqual(self.b2.user_id, "")

    def test_name(self):
        self.assertTrue(hasattr(self.b2, "name"))
        self.assertEqual(self.b2.name, "")

    def test_description(self):
        self.assertTrue(hasattr(self.b2, "description"))
        self.assertEqual(self.b2.description, "")

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.b2, "number_rooms"))
        self.assertEqual(self.b2.number_rooms, 0)

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.b2, "number_bathrooms"))
        self.assertEqual(self.b2.number_bathrooms, 0)

    def test_max_guest(self):
        self.assertTrue(hasattr(self.b2, "max_guest"))
        self.assertEqual(self.b2.max_guest, 0)

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.b2, "price_by_night"))
        self.assertEqual(self.b2.price_by_night, 0)

    def test_latitude(self):
        self.assertTrue(hasattr(self.b2, "latitude"))
        self.assertEqual(self.b2.latitude, 0.0)

    def test_longitude(self):
        self.assertTrue(hasattr(self.b2, "longitude"))
        self.assertEqual(self.b2.longitude, 0.0)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.b2, "amenity_ids"))
        self.assertEqual(self.b2.amenity_ids, [])
