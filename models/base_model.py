#!/usr/bin/python3
"""
Module that contain BaseModel class
"""
from datetime import datetime
import uuid
import models
import uuid


class BaseModel:
    """
    BaseModel class for all other classes
    """

    def __init__(self, *args, **kwargs):
        """ initialization """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ String """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictonary """
        aux_dict = self.__dict__.copy()
        aux_dict["__class__"] = self.__class__.__name__
        aux_dict["created_at"] = self.created_at.isoformat()
        aux_dict["updated_at"] = self.updated_at.isoformat()
        return aux_dict
