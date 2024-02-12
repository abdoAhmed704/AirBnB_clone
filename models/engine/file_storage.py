#!/usr/bin/python3
"""
the class that handel the json file
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        prints all
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        add new
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        save to json file
        """
        obj_dictionary = {}
        for obj in FileStorage.__objects.keys():
            obj_dictionary[obj] = FileStorage.__objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dictionary, f)

    def reload(self):
        """
        load from json
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dictionary = json.load(f)

                for k, v in obj_dictionary.items():
                    cls_name, object_id = k.split('.')

                    cls = eval(cls_name)

                    inst = cls(**v)

                    FileStorage.__objects[k] = inst
