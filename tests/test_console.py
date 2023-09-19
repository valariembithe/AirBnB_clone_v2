#!/usr/bin/python3
"""Test console module """

import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestCreateCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_with_valid_arguments(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel name=\"Test Object\"")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output != "")

    def test_create_with_missing_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_with_invalid_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create InvalidClass")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")


if __name__ == '__main__':
    unittest.main()
