#!/usr/bin/python3

from unittest import TestCase
from models.city import City
from datetime import datetime


class TestCity(TestCase):
    def setUp(self):
        self.b1 = City()
        self.b1.created_at = datetime.now()
        self.b1.updated_at = datetime.now()
        self.b2 = City()

    def test_id(self):
        self.model_test = City()
        self.assertNotEqual(self.b1.id, self.model_test.id)

    def test_save(self):
        updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(updated_at, self.b1.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("City.{}".format(self.b1.id), file.read())

    def test_to_dict(self):
        new = self.b1.to_dict()
        self.assertEqual(new["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.b1.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.b1.__class__.__name__)

    def test__str__(self):
        className = self.b1.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.b1.id, self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())

    def test_state_id(self):
        self.assertTrue(hasattr(self.b2, "state_id"))
        self.assertEqual(self.b2.state_id, "")

    def test_name(self):
        self.assertTrue(hasattr(self.b2, "name"))
        self.assertEqual(self.b2.name, "")
