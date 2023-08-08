#!/usr/bin/python3

""" program entry point """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ a method that quite the console """
        return True
    """
    def do_emptyline(self):
        # a method that overrides when an emptyline and enter 
        print('\n')
        return cmd.Cmd.emptyline(self)
    """

    def do_EOF(self, line):
        """ a method that Exit the console """
        return True


if '__name__' == '__main__':
    HBNBCommand().cmdloop()
