#!/usr/bin/python3

from unittest import TestCase
from models.review import Review
from datetime import datetime


class TestReview(TestCase):
    def setUp(self):
        self.b1 = Review()
        self.b1.created_at = datetime.now()
        self.b1.updated_at = datetime.now()
        self.b2 = Review()

    def test_id(self):
        self.model_test = Review()
        self.assertNotEqual(self.b1.id, self.model_test.id)

    def test_save(self):
        updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(updated_at, self.b1.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("Review.{}".format(self.b1.id), file.read())

    def test_to_dict(self):
        new = self.b1.to_dict()
        self.assertEqual(new["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.b1.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.b1.__class__.__name__)

    def test__str__(self):
        className = self.b1.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.b1.id, self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())

    def test_place_id(self):
        self.assertTrue(hasattr(self.b2, "place_id"))
        self.assertEqual(self.b2.place_id, "")

    def test_user_id(self):
        self.assertTrue(hasattr(self.b2, "user_id"))
        self.assertEqual(self.b2.user_id, "")

    def test_text(self):
        self.assertTrue(hasattr(self.b2, "text"))
        self.assertEqual(self.b2.text, "")
