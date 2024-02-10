#!/usr/bin/python3
import datetime
import uuid
from . import storage


class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            class_name = kwargs.pop("__class__", None)
            for key, val in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    cp = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.datetime.strptime(val, cp))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        storage.new(self)
        print("A777AAA")

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        class_name = self.__class__.__name__
        new_created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict = self.__dict__.copy()
        updates = {
            "__class__": class_name,
            "created_at": new_created_at,
            "updated_at": new_updated_at
        }
        my_dict.update(updates)
