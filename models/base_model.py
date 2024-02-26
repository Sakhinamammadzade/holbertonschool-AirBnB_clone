#!/usr/bin/python3
""""BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """Define model"""
    def __init__(self):
        """Base class constructor"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Str method"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """save memory"""
        self.created_at = datetime.now()

    def to_dict(self):
        """Dict"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
