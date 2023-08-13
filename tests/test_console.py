#!/usr/bin/python3
<<<<<<< HEAD
=======
"""Testing the console, for all features!"""


from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")


if __name__ == '__main__':
    HBNBCommand().unittest()
>>>>>>> 80c5be6c305a1552ce766ee6f31cc789e40e971a
