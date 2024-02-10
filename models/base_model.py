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

        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """

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
        
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print(my_model is my_new_model)
