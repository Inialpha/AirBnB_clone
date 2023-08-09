#!/usr/bin/python3

""" program entry point """
from models.base_model import BaseModel
import cmd
import models
import sys


class HBNBCommand(cmd.Cmd):

    all_classes = ["BaseModel", "User"]
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ a method that overrides when an emptyline when enter key
            is press"""
        pass

    def do_EOF(self, line):
        """ a method that Exit the console """
        return True

    def do_create(self, cls):
        """Creates a new instance of BaseModel, saves it (to the JSON file)"""
        if cls:
            if cls in self.all_classes:
                my_class = getattr(sys.modules[__name__], cls)
                obj = my_class()
                print(obj.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in self.all_classes:
            my_dict = models.storage.all()
            key = args[0] + "." + args[1]
            if key in my_dict:
                print(my_dict[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] in self.all_classes:
            key = args[0] + "." + args[1]
            my_dict = models.storage.all()
            if key in my_dict:
                del (my_dict[key])
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
