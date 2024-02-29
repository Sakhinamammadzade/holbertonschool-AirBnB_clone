#!/usr/bin/python3
from unittest import TestCase
from models.base_model import BaseModel

class TestBaseModel(TestCase):
    def setUp(self):
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.created_at = self.b1.created_at.isoformat()
        self.updated_at = self.b1.updated_at.isoformat()
    
    def test_atributes(self):
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_save(self):
        updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(updated_at, self.b1.updated_at)

    def test_to_dict(self):
        new = self.b1.to_dict()
        self.assertEqual(new["created_at"], self.created_at)
        self.assertEqual(new["updated_at"], self.updated_at)
        self.assertEqual(new['__class__'], BaseModel.__name__)

    def test__str__(self):
        className = BaseModel.__name__
        result = "[{}] ({}) {}".format(className, self.b1.id, self.b1.__dict__)
        self.assertEqual(result, self.b1.__str__())
