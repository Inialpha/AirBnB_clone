#!/usr/bin/python3

""" program entry point """

import cmd


class HBNBCommand(cmd.Cmd):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
