#!/usr/bin/python3

""" program entry point """
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import cmd
import sys


class HBNBCommand(cmd.Cmd):

    all_classes = ["BaseModel", "User", "Place", "State", "City",
                   "Amenity", "Review"]
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
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation
        of all instances based or not on the class name."""
        my_dict = models.storage.all()
        all_list = []
        if len(arg) == 0:
            for key in my_dict:
                all_list.append(str(my_dict[key]))
        else:
            if arg in self.all_classes:
                for key, value in my_dict.items():
                    if arg == value.to_dict()["__class__"]:
                        all_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return
        print(all_list)

    def do_update(self, arg):
        """Updates an instance based on the
        class name and id by adding or updating attribute"""

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif args[0] in self.all_classes:
            key = args[0] + "." + args[1]
            my_dict = models.storage.all()
            if key in my_dict:
                if hasattr(my_dict[key], args[2]):
                    a_type = type(getattr(my_dict[key], args[2]))
                    args[3] = a_type(args[3])
                setattr(my_dict[key], args[2], args[3])
                models.storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")
    
    def precmd(self, line):
        """precmd method"""
        _parts = line.split('.', 1)
        if len(_parts) == 2:
            _class = _parts[0]
            _args = _parts[1].split('(', 1)
            _cmd = _args[0]
            new_line = _cmd + " " + _class
            return new_line
        return line

    def do_count(self, cls):
        """ Retrieves the number of instances of a class """
        if cls:
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
