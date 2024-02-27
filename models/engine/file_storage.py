#!/usr/bin/python3
"""FileStorage class"""

import json
from models.base_model import BaseModel


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
        FileStorage.__objects["{} {}".format(cname, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for k in FileStorage.__objects:
            new_dict[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, "w") as file_path:
            json.dump(new_dict, file_path)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file_path:
                objdict = json.load(file_path)
                FileStorage.__objects = {}
                for k in objdict:
                    FileStorage.__objects[k] = new_dict[k.split(".")[0]](**objdict[key])
        except Exception:
            pass


