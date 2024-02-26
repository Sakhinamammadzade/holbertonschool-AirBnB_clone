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
        return f'[{type(self).__name__}] {self.id} {self.__dict__}'

    def save(self):
        """save memory"""
        self.created_at = datetime.now()

    def to_dict(self):
        """Dict"""
        result = {'__class__': self.__class__.__name__}
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = instance_dict['created_at'].isoformat()
        instance_dict['updated_at'] = instance_dict['updated_at'].isoformat()
        return instance_dict
