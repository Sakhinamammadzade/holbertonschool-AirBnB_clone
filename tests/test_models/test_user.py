#!/usr/bin/python3

from unittest import TestCase
from models.user import User
from datetime import datetime


class TestUser(TestCase):
    def setUp(self):
        self.b1 = User()
        self.b1.created_at = datetime.now()
        self.b1.updated_at = datetime.now()
        self.user = User()

    def test_id(self):
        self.model_test = User()
        self.assertNotEqual(self.b1.id, self.model_test.id)

    def test_save(self):
        updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(updated_at, self.b1.updated_at)
        with open("file.json", "r") as file:
            self.assertIn("User.{}".format(self.b1.id), file.read())

    def test_to_dict(self):
        new = self.b1.to_dict()
        self.assertEqual(new["created_at"], self.b1.created_at.isoformat())
        self.assertEqual(new["updated_at"], self.b1.updated_at.isoformat())
        self.assertEqual(new['__class__'], self.b1.__class__.__name__)

    def test__str__(self):
        className = self.b1.__class__.__name__
        result = "[{}] ({}) {}".format(className, self.b1.id, self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())

    def test_email(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_password(self):
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_first_name(self):
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_last_name(self):
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")
