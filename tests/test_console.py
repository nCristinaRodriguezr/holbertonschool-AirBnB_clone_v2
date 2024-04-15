#!/usr/bin/python3
"""Test console.py"""
import os
import uuid
import unittest
from models.__init__ import storage
from models.base_model import BaseModel
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


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
        self.assertEqual(output.strip(), "Exits program without formatting")

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
        self.base.save()
        self.assertEqual(len(storage.all()), 1)  # Check if object is stored
        self.capture_stdout("destroy BaseModel {}".format(self.base.id))
        self.assertEqual(len(storage.all()), 0)  # Check if object is removed

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
        self.base.save()
        output = self.capture_stdout("count BaseModel")
        self.assertEqual(output.strip(), "1")

    def test_update(self):
        """Test update method"""
        self.base.save()
        self.capture_stdout("update BaseModel{} name Test"
                            .format(self.base.id))
        self.assertEqual(self.base.name, "Test")


if __name__ == '__main__':
    unittest.main()
