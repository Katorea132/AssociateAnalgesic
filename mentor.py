#!/usr/bin/python3
"""
This module contains the Mentor class, in charge of keeping track
of which day and timeset a mentor has avaliable
"""


class Mentor:
    """
    This is the Mentor class, each instance contains the basic
    information of a different mentor, it is also used to
    match avaliable times with a startup.
    """
    __valid_days = {
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Undefined"
    }
    __valid_times = {
        "AM", "PM", "Undefined"
    }

    def __init__(self, name, day, time):
        self.name = name
        self.day = day
        self.time = time
        self.__hours_avaliable()

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if day in self.__valid_days:
            self.__day = day
        else:
            raise ValueError("Not a day between monday and friday")

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        if time in self.__valid_times:
            self.__time = time
        else:
            raise ValueError("Not AM, PM or Undefined")

    def __hours_avaliable(self):
        """
        Sets correctly the time frame for a given mentor
        """
        if self.time == "AM":
            self.hours = {
                "9:10": [False, None, "9:30"],
                "9:30": [False, None, "9:50"],
                "9:50": [False, None, "10:10"],
                "10:10": [False, None, "10:30"],
                "10:30": [False, None, "10:50"],
                "10:50": [False, None, "11:10"],
                "11:10": [False, None, "11:30"],
                "11:30": [False, None, "11:50"],
                "11:50": [False, None, "12:10"],
                "12:10": [False, None, "12:30"]
            }
        elif self.time == "PM":
            self.hours = {
                "13:10": [False, None, "13:30"],
                "13:30": [False, None, "13:50"],
                "13:50": [False, None, "14:10"],
                "14:10": [False, None, "14:30"],
                "14:50": [False, None, "15:10"],
                "15:10": [False, None, "15:30"],
                "15:30": [False, None, "15:50"],
                "15:50": [False, None, "16:10"],
                "16:10": [False, None, "16:30"]
            }
        else:
            self.hours = {
                "Undefined": [True, "", "Undefined"],
            }

    def is_avaliable(self, time):
        """Determiens whether or not a time lapse is avaliable, by accessing\
        the first value in the list of each hour, which is set to false when\
        not taken and true when taken

        Args:
            time (str): A string containing the time in military date format

        Returns:
            bool: True or False if its avaliable or not, respectively
            Always True for Undefined cases
        """
        if time == "Undefined" or not self.hours:
            return True
        return not self.hours[time][0]

    def occupy_hours(self, time, startup):
        """Populates a hour to appear taken with the name
        of the startup, it also sets the first value in the hour list
        to mark it as taken (thus, setting the value to True)

        On Undefined, the companies names will be added together on a single
        string, separated by forward slasehs '/'

        Args:
            hour (str): time to populate, in military date format
            startup (str): name of the startup
        """
        if time == "Undefined":
            self.hours["Undefined"][1] += startup + "/"
        elif self.is_avaliable(time):
            self.hours[time][0] = True
            self.hours[time][1] = startup
