#!/usr/bin/python3
"""module for the console test cases"""
import console
from console import HBNBCommand
import unittest
import io


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

#    def setUp(self):
#       """sets up for each test"""
#
#       self.output = io.StringIO()
#       sys.stdout = self.output

    def test_create(self):
        """test create command"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(f.getvalue() > 0))
