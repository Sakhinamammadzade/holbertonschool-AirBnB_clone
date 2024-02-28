#!/usr/bin/python3
"""FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for k in self.__objects:
            new_dict[k] = self.__objects[k].to_dict()
        with open(self.__file_path, "w") as file_path:
            json.dump(new_dict, file_path)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file_path:
                objdict = json.load(file_path).items()
                for k, v in objdict:
                    v  = eval(k.split(".")[0])(**v)
                    self.__objects[k] = v
        except Exception:
            pass
