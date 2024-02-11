#!/usr/bin/python3
"""
Module for baseModel
"""
import uuid
import datetime
import models


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        """
        init of the class
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    text = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.datetime.strptime(value, text))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        save to json file
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        good dictionary
        """
        my_dict = self.__dict__.copy()
        updates = {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        my_dict.update(updates)
        return my_dict

    def __str__(self):
        """
        good represntation
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"
