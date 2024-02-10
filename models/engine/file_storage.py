#!/usr/bin/python3
import json
from ..base_model import BaseModel


class FileStorage:
    def __init__(self) -> None:
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        objs = {}
        for obj in self.__objects.keys():
            objs[obj] = self.__objects[obj].to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objs, f)

    def reload(self):
        import os
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                try:
                    objs_json = json.load(f)
                    self.__objects.update(objs_json)
                except Exception:
                    pass
