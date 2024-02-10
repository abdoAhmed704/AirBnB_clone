#!/usr/bin/python3
""" console """
import cmd


class HBNBCommand(cmd.Cmd):
    "Documented commands (type help <topic>):"

    prompt = "(hbnb)"

    def do_quit(self, args):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_EOF(self, arg):
        """Exits console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
