#!/usr/bin/python3
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

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """

        """
        return FileStorage.__objects

    def new(self, obj):
        """

        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """

        """
        obj_dictionary = {}
        for obj in FileStorage.__objects.keys():
            obj_dictionary[obj] = FileStorage.__objects[obj].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dictionary, f)

    def reload(self):
        """

        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dictionary = json.load(f)

                    for k, v in obj_dictionary.items():
                        cls_name, object_id = k.split('.')

                        cls = eval(cls_name)

                        inst = cls(**v)

                        FileStorage.__objects[k] = inst
                except Exception:
                    pass
