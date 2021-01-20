#!/usr/bin/python3
"""
Module containing unit tests for most of the methods
in the Mentor class
"""

from mentor import Mentor
import unittest


class TestMentor(unittest.TestCase):
    """Class to test Mentor class"""

    def test_mentor_correct_init(self):
        """
        Tests the correct initialization and parametization of a mentor object
        """
        a = Mentor("pizza", "Monday", "AM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Monday", a.day)
        self.assertEqual("AM", a.time)
        a = Mentor("pizza", "Undefined", "Undefined")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Undefined", a.day)
        self.assertEqual("Undefined", a.time)
        a = Mentor("pizza", "Tuesday", "AM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Tuesday", a.day)
        self.assertEqual("AM", a.time)
        a = Mentor("pizza", "Wednesday", "AM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Wednesday", a.day)
        self.assertEqual("AM", a.time)
        a = Mentor("pizza", "Thursday", "AM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Thursday", a.day)
        self.assertEqual("AM", a.time)
        a = Mentor("pizza", "Friday", "AM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Friday", a.day)
        self.assertEqual("AM", a.time)
        a = Mentor("pizza", "Monday", "PM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Monday", a.day)
        self.assertEqual("PM", a.time)
        a = Mentor("pizza", "Tuesday", "PM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Tuesday", a.day)
        self.assertEqual("PM", a.time)
        a = Mentor("pizza", "Wednesday", "PM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Wednesday", a.day)
        self.assertEqual("PM", a.time)
        a = Mentor("pizza", "Thursday", "PM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Thursday", a.day)
        self.assertEqual("PM", a.time)
        a = Mentor("pizza", "Friday", "PM")
        self.assertTrue(a)
        self.assertEqual("pizza", a.name)
        self.assertEqual("Friday", a.day)
        self.assertEqual("PM", a.time)

    def test_mentor_missing_one_init(self):
        """
        Tests the correct raise of TypeError when missing 1 parameter of init
        """
        with self.assertRaises(TypeError):
            a = Mentor("pizza", "Monday")

    def test_mentor_missing_two_init(self):
        """
        Tests the correct raise of TypeError when missing 2 parameters of init
        """
        with self.assertRaises(TypeError):
            a = Mentor("pizza")

    def test_mentor_missing_three_init(self):
        """
        Tests the correct raise of TypeError when missing 3 parameters of init
        """
        with self.assertRaises(TypeError):
            a = Mentor()

    def test_mentor_wrong_day_init(self):
        """
        Tests the correct raise of ValueError on invalid day
        """
        self.assertRaises(ValueError, Mentor, "pizza", "Mondayayaya", "AM")
        self.assertRaises(ValueError, Mentor, "pizza", "", "AM")
        self.assertRaises(ValueError, Mentor, "pizza", "MMonday", "AM")
        self.assertRaises(ValueError, Mentor, "pizza", "MOnday", "AM")
        self.assertRaises(ValueError, Mentor, "pizza", "", "AM")
        self.assertRaises(ValueError, Mentor, "pizza", 3, "AM")
        self.assertRaises(ValueError, Mentor, "pizza", "NotPizza", "AM")

    def test_mentor_wrong_time_init(self):
        """
        Tests the correct raise of ValueError on invalid time frame
        """
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "AMM")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "AMM")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "AAM")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "Am")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "aM")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "ma")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", "")
        self.assertRaises(ValueError, Mentor, "pizza", "Monday", 3)

    def test_mentor_is_avaliable_correct_returns(self):
        """
        Tests for the appropiated return of the is avaliable function
        """
        a = Mentor("pizza", "Monday", "AM")
        self.assertTrue(a.is_avaliable("9:30"))
        a.hours["9:30"][0] = True
        self.assertFalse(a.is_avaliable("9:30"))

    def test_mentor_correct_time_frame_assigned(self):
        """
        Tests that the correct frame and only that frame was assigned to\
the mentor
        """
        a = Mentor("pizza", "Monday", "AM")
        self.assertTrue(a.is_avaliable("9:30"))
        self.assertRaises(KeyError, a.is_avaliable, "14:50")
        a = Mentor("pizza", "Monday", "PM")
        self.assertTrue(a.is_avaliable("14:50"))
        self.assertRaises(KeyError, a.is_avaliable, "9:50")

    def test_mentor_correct_resting_time(self):
        """
        Tests that no meeting is possible in the resting time (14:30-14:50)
        """
        a = Mentor("pizza", "Monday", "PM")
        self.assertRaises(KeyError, a.is_avaliable, "14:30")

    def test_mentor_correct_space_between_time_frames(self):
        """
        Tests that no meeting is possible in the time between time frames
        """
        a = Mentor("pizza", "Monday", "PM")
        self.assertRaises(KeyError, a.is_avaliable, "16:30")
        a = Mentor("pizza", "Monday", "AM")
        self.assertRaises(KeyError, a.is_avaliable, "12:50")

    def test_mentor_occupy_hours_non_undefined(self):
        """
        Tests that the Occupy hours function does populate correctly\
the hour and company name when non undefined values are given
        """
        a = Mentor("pizza", "Monday", "AM")
        a.occupy_hours("9:30", "Pepsiman")
        self.assertTrue(a.hours["9:30"][0])
        self.assertEqual(a.hours["9:30"][1], "Pepsiman")
        self.assertFalse(a.is_avaliable("9:30"))

    def test_mentor_occupy_hours_on_undefined(self):
        """
        Tests that Occupy hours function does populate correctly\
when undefined is present
        """
        a = Mentor("pizza", "Undefined", "Undefined")
        a.occupy_hours("Undefined", "Damedanedameyodamenanoyo")
        self.assertEqual(a.hours["Undefined"][1], "Damedanedameyodamenanoyo/")
        a.occupy_hours("Undefined", "Antagasugitesugisugite")
        self.assertEqual(a.hours["Undefined"][1],
                         "Damedanedameyodamenanoyo/Antagasugitesugisugite/")

    def test_mentor_occupy_hours_on_invalid_time(self):
        """
        Tests that Occupy does in fact throw a KeyError when\
given an invalid hour
        """
        a = Mentor("pizza", "Monday", "AM")
        self.assertRaises(KeyError, a.occupy_hours, "14:30", "Lala")
