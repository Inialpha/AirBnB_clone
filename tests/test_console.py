#!/usr/bin/python3
"""Testing the console, for all features!"""


from unittest.mock import patch
from io import StringIO
import unittest
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Testing all the implemented functionality in console"""
    
    def setUp(self):
        """Setting up the console"""
        self.fake_stdout = StringIO()
        self.patcher = patch('sys.stdout', new=self.fake_stdout)
        self.patcher.start()

    def test_quit_command(self):
        """Test quit command"""
        HBNBCommand().onecmd("quit")
        output = self.fake_stdout.getvalue()
        self.assertIsNotNone(output)

    def tearDown(self):
        """Tear down the console"""
        self.patcher.stop()


if __name__ == '__main__':
    unittest.main()
