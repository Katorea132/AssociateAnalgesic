#!/usr/bin/python3
"""
Module containing unit tests for most of the functions
in date sanitazer module
"""

from datesanitazer import day_date
import unittest


class TestDateSanitazer(unittest.TestCase):
    """Class to test Date Sanitazer"""

    def test_day_date_format(self):
        """
        Tests that the day date funciton returns
        the expected date format yyyy/mm/dd
        """
        self.assertRegex(day_date("Monday"),
                         r"^\d\d\d\d\/(0?[1-9]|1[0-2])\/(0?[1-9]|[1-3][0-9])$")

    def test_day_date_undefined(self):
        """
        Expects Undefined to be returned when Undefined is passed
        """
        self.assertEqual("Undefined", day_date("Undefined"))

    def test_day_key_error(self):
        """
        Checks for a key error when the wrong input is given
        """
        self.assertRaises(KeyError, day_date, "pizza")
        self.assertRaises(KeyError, day_date, "Mondayayaya")
        self.assertRaises(KeyError, day_date, "MOnday")
        self.assertRaises(KeyError, day_date, "MMonday")
        self.assertRaises(KeyError, day_date, "monday")
        self.assertRaises(KeyError, day_date, "")
        self.assertRaises(KeyError, day_date, 3)
