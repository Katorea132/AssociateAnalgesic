#!/usr/bin/python3
"""
Module containing unit tests for some of the functions
in the magicdoer module
"""

import csv
from magicdoer import are_available, assign_them_all
from startup import Startup
from mentor import Mentor
from datesanitazer import day_date
import unittest


class TestMentor(unittest.TestCase):
    """Class to test magicdoer module"""

    def test_magicdoer_are_available(self):
        """
        Tests that what are available answers is in fact what\
is available of both mentor and startup are answering
        """
        a = Mentor("Pizza", "Tuesday", "AM")
        b = Startup("Pepsiman")
        self.assertEqual(a.is_available("9:30")
                         and b.is_available("Tuesday", "9:30"),
                         are_available(a, b, "9:30"))
        a.hours["9:30"][0] = True
        self.assertEqual(a.is_available("9:30")
                         and b.is_available("Tuesday", "9:30"),
                         are_available(a, b, "9:30"))
        b.slots["Tuesday"]["9:50"][0] = True
        self.assertEqual(a.is_available("9:50")
                         and b.is_available("Tuesday", "9:50"),
                         are_available(a, b, "9:50"))

    def test_magicdoer_assign_them_all_without_file(self):
        """
        This tests that the FIleNotFoundError is raised on missing file \
which could also happen if the file had a different name\
This test will fail if the file is in fact present
        """
        self.assertRaises(FileNotFoundError, assign_them_all, {}, {})
