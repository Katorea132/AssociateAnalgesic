#!/usr/bin/python3
"""
This module contains the Startup class, in charge of keeping track
of avaliable times for each startup
"""


class Startup:
    """
    This is the Startup class, each instance contains the basic information
    of a different startup, it is also used to match
    avaliable times with a mentor.
    """
    def __init__(self, name):
        self.slots = {
            "Monday": {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"],
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            },
            "Tuesday": {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"],
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            },
            "Wednesday": {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"],
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            },
            "Thursday": {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"],
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            },
            "Friday": {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"],
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            },
        }
        self.name = name

    def is_avaliable(self, day, time):
        """Determines whether or not a time frame has been set or not,
        Always False for Undefined cases

        Args:
            day (str): The day of the meeting, full name of the day
            time (str): The hour of the meeting, military date format

        Returns:
            bool: True or False if it has been or has been not taken
        """
        if time == "Undefined" or day == "Undefined":
            return False
        return not self.slots[day][time][0]

    def occupy_hours(self, day, time, mentor):
        """Populates an hour and day to appear taken with the
        name of the mentor.

        Args:
            day (str): Day, written by its name ex: 'Monday'
            time (str): time to populate, in military date format
            mentor (str): Name of the mentor
        """
        self.slots[day][time][0] = True
        self.slots[day][time][1] = mentor
