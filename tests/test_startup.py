#!/usr/bin/python3
"""
Module containing unit tests for most of the methods
in the Startup class
"""

from startup import Startup
import unittest


class TestMentor(unittest.TestCase):
    """Class to test Startup class"""

    def test_startup_correct_init(self):
        """
        Tests the correct initialization and parametization of a startup object
        """
        a = Startup("pizza")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertTrue(a.slots)

    def test_startup_missing_one_init(self):
        """
        Tests the correct raise of TypeError when missing 1 parameter of init
        """
        with self.assertRaises(TypeError):
            a = Startup()

    def test_is_avaliable_returns_correctly(self):
        """
        It should return True if the hour and day combination are empty\
for Undefined it is always False
        """
        a = Startup("Pepsiman")
        self.assertTrue(a.is_avaliable("Tuesday", "9:30"))
        a.slots["Tuesday"]["9:30"][0] = True
        self.assertFalse(a.is_avaliable("Tuesday", "9:30"))
        self.assertFalse(a.is_avaliable("Undefined", "Undefined"))

    def test_occupy_hours_assigns_correctly(self):
        """
        Tests that occupy hours does indeed populate and assigns hours\
correctly
        """
        a = Startup("Pepsiman")
        self.assertTrue(a.is_avaliable("Tuesday", "9:30"))
        a.occupy_hours("Tuesday", "9:30", "pizza")
        self.assertFalse(a.is_avaliable("Tuesday", "9:30"))
        self.assertEqual(a.slots["Tuesday"]["9:30"][1], "pizza")
        self.assertTrue(a.slots["Tuesday"]["9:30"][0])
