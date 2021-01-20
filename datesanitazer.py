#!usr/bin/python3
"""
This module handles the logic to pick the appropiate date
to start scheduling (The week after the execution of this program)
the meetings between mentors and startups
"""

import datetime


def day_date(day):
    """Determines the date for a given day on the next week

    Args:
        day (string): From monday to friday, days are represented
        from 0 to 4 respectively

    Returns:
        date: returns a date object with format yyyy/mm/dd
    """
    if day == "Undefined":
        return ("Undefined")
    days = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4
        }
    current_day = datetime.datetime.now().date()
    days_ahead = days[day] - current_day.weekday() + 7
    return (current_day + datetime.timedelta(days_ahead)).strftime("%Y/%m/%d")
