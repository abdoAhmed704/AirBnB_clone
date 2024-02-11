#!/usr/bin/python3
"""
console
"""
import cmd
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    "Documented commands (type help <topic>):"

    prompt = "(hbnb)"
    my_class = ["BaseModel"]

    def do_quit(self, args):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_create(self, args):
        """
        creat an instance of a given class
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        else:
            intance = eval("BaseModel()")
            FileStorage.save(intance)
            print(intance.id)

    def do_show(self, args):
        """
        show all the obj
        """
        commands = shlex.split(args)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            objs_storage = storage.all()
            search_key = f"{commands[0]}.{commands[1]}"
            if search_key in objs_storage:
                print(objs_storage[search_key])
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        show all the storage
        """
        objs_storage = storage.all()
        coms = shlex.split(args)

        if len(coms) == 0:
            for v in objs_storage.values():
                print(str(v))
        elif coms[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        else:
            for k, v in objs_storage.items():
                if coms[0] == k.split('.')[0]:
                    print(str(v))

    @staticmethod
    def is_id(objs_storage, class_id):
        if class_id in objs_storage:
            return True

    def do_update(self, args):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>
        """
        coms = shlex.split(args)
        objs_storage = storage.all()
        if len(coms) == 0:
            print("** class name missing **")
        elif coms[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
        elif len(coms) == 1:
            print("** instance id missing **")
        elif not self.is_id(objs_storage, f"{coms[0]}.{coms[1]}"):
            print("** no instance found **")
        elif len(coms) == 2:
            print("** attribute name missing **")
        elif len(coms) == 3:
            print("** value missing **")
        else:
            for k, v in objs_storage.items():
                if coms[0] == k.split('.')[0]:
                    instance = objs_storage[f"{coms[0]}.{coms[1]}"]
                    setattr(instance, str(coms[2]), coms[3])
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
