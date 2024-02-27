#!/usr/bin/python3
""""BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Define model"""
    def __init__(self, *args, **kwargs):
        """Base class constructor"""
        if len(kwargs) != 0:
            forma = "%Y-%m-%dT%H:%M:%S.%f"
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(kwargs[k], forma)
                    setattr(self, k, v)
                elif k != "__class__":
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Str method"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """save memory"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dict"""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
