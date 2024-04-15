#!/usr/bin/python3
"""Test console"""
from models.base_model import BaseModel, Base
import os
import uuid
import unittest
from io import StringIO
import sys
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from console import storage


class TestHBNBCommand(unittest.TestCase):
    """Unittesting the HBNB command interpreter"""

    def setUp(self):
        self.console = HBNBCommand()
        self.base = BaseModel()

    def tearDown(self):
        del self.console
        del self.base

    def capture_stdout(self, command):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.console.onecmd(command)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    def test_help_quit(self):
        """Test help message for quit command"""
        output = self.capture_stdout("help quit")
        self.assertEqual(output.strip(), "Exits the program with formatting")

    def test_help_EOF(self):
        """Test help message for EOF command"""
        output = self.capture_stdout("help EOF")
        self.assertEqual(output.strip(),
                         "Exits the program without formatting")

    def test_create(self):
        """Test create method"""
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output.strip()) == 36)  # Check if UUID is printed

    def test_show(self):
        """Test show method"""
        self.base.save()
        output = self.capture_stdout("show BaseModel {}".format(self.base.id))
        self.assertIn(self.base.__str__(), output)

    def test_destroy(self):
        """Test destroy method"""
        storage.reload()
        initial_count = len(storage.all())
        self.base.save()
        self.assertEqual(len(storage.all()), initial_count + 1)
        self.capture_stdout("destroy BaseModel {}".format(self.base.id))
        self.assertEqual(len(storage.all()), initial_count)

    def test_all(self):
        """Test all method"""
        self.base.save()
        output = self.capture_stdout("all")
        self.assertIn(self.base.__str__(), output)

    def test_all_with_classname(self):
        """Test all method with class name"""
        self.base.save()
        output = self.capture_stdout("all BaseModel")
        self.assertIn(self.base.__str__(), output)

    def test_count(self):
        """Test count method"""
        keys = list(storage.all().keys())
        for key in keys:
            del storage.all()[key]
        base1 = BaseModel()
        base2 = BaseModel()
        base3 = BaseModel()
        base1.save()
        base2.save()
        base3.save()
        output = self.capture_stdout("count BaseModel")
        self.assertEqual(output.strip(), "3")

    def test_update(self):
        """Test update command input."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.console.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n", f.getvalue())


if __name__ == '__main__':
    unittest.main()
