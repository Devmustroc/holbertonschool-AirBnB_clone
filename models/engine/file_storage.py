#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ initialization """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        if obj:
            FileStorage.__objects[obj.__class__.__name__ +
                                  "." + str(obj.id)] = obj

    def save(self):
        """ serializes objectss to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, f)

    def reload(self):
        """ Reload the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = eval(
                        val["__class__"])(**val)
