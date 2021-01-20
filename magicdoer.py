#!/usr/bin/python3
"""
This module contains the magic, it is in charge of finding,
assigning and validating the dates for both a mentor
and a startup, printing and saving for reference the information
"""


import csv
from startup import Startup
from mentor import Mentor
from datesanitazer import day_date


def are_avaliable(mentor, start, time):
    """Tells if the hour and day are valid for both mentor and startup

    Args:
        mentor (obj): A mentor object
        start (obj): A startup object
        time (str): Time in military date format

    Returns:
        bool: True or false depending on if the time is valid for both or not
    """
    return mentor.is_avaliable(time) and start.is_avaliable(mentor.day, time)


def match_them_all(mentor, startup):
    """Finds a valid hour to assign to both the company and mentor,
    populates the respecting object for future references to avoid
    collisions on the meeting times.

    Args:
        mentor (obj): A mentor object
        startup (obj): A startup object
    """
    morning_birds = ["9:10", "9:30", "9:50", "10:10",
                     "10:30", "10:50", "11:10", "11:30",
                     "11:50", "12:10"]
    night_owls = ["13:10", "13:30", "13:50", "14:10",
                  "14:50", "15:10", "15:30", "15:50",
                  "16:10"]
    if mentor.time == "AM":
        for time in morning_birds:
            if (are_avaliable(mentor, startup, time)):
                mentor.occupy_hours(time, startup.name)
                startup.occupy_hours(mentor.day, time, mentor.name)
                break
    elif mentor.time == "PM":
        for time in night_owls:
            if (are_avaliable(mentor, startup, time)):
                mentor.occupy_hours(time, startup.name)
                startup.occupy_hours(mentor.day, time, mentor.name)
                break
    else:
        mentor.occupy_hours("Undefined", startup.name)


def assign_them_all(mentors, startups):
    """This function reads from the data.csv file in the same folder
    line by line, assuming the following order of items:
    Name (of the mentor), day he is avaliable, Time frame (AM or PM),
    Company1, Company2,...
    and call for the match_them_all function to populate the appropiate
    objects

    Args:
        mentors ([type]): [description]
        startups ([type]): [description]
    """
    with open("./data.csv", "r") as f:
        file = csv.reader(f)
        file.__next__()
        for rows in file:
            row = list(rows)
            current_mentor = Mentor(row[0], row[1].strip(" "),
                                    row[2].strip(" "))
            mentors[row[0]] = current_mentor
            for i in range(3, len(row)):
                if row[i]:
                    if row[i] not in startups:
                        startups[rows[i]] = Startup(row[i])
                    current_startup = startups[row[i]]
                    match_them_all(current_mentor, current_startup)


def print_them_all(mentors):
    """A function that prints all the mentor meetings
    with it's respective time and startup

    Args:
        mentors (dict): Dictionary of mentor objects
    """
    for mentor in mentors.values():
        print(mentor.name, "-", mentor.day)
        final_hour = len(mentor.hours)
        counter = 0
        for hour, values in mentor.hours.items():
            if values[0]:
                if counter != 0:
                    print(", ", end='')
                else:
                    counter += 1
                print(values[1], "-", hour, end='')
        print("\n")


def save_them_all(mentors, startups):
    """This function saves all the mentors schedule in a cvs file, ordered by
    order of appearance and time of meetings, in the original csv file,
    Mentors with undefined times only take 1 line in the file

    It also saves each startup schedules, with both taken and free time slots
    for the each day, there is no order in which they are created but
    each file internally shows the times in order both in days and hours

    Args:
        mentors (dict): Dictionary of objects of mentors
        startups (dict): Dictionary of objects of startups
    """
    with open("mentors_schedule.csv", "w") as f:
        field_names = [
            "Mentor Name", "Meeting Day", "Time Frame",
            "Company Name", "Starting Hour", "Finishing Hour"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for mentor in mentors.values():
            sanitizedDate = day_date(mentor.day)
            for hour, values in mentor.hours.items():
                if hour != "Undefined":
                    writer.writerow({
                        "Mentor Name": mentor.name,
                        "Meeting Day": mentor.day,
                        "Time Frame": mentor.time,
                        "Company Name": values[1],
                        "Starting Hour": sanitizedDate + " " + hour,
                        "Finishing Hour": sanitizedDate + " " + values[2]
                    })
                else:
                    writer.writerow({
                        "Mentor Name": mentor.name,
                        "Meeting Day": mentor.day,
                        "Time Frame": mentor.time,
                        "Company Name": values[1],
                        "Starting Hour": "Undefined",
                        "Finishing Hour": "Undefined"
                    })
    field_names = [
        "Company Name", "Day", "Starting Hour",
        "Finishing Hour", "Assigned with"]
    for startup in startups.values():
        with open(startup.name.replace(" ", "_") + ".csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            for day, hours in startup.slots.items():
                for hour, values in hours.items():
                    writer.writerow({
                        "Company Name": startup.name,
                        "Day": day,
                        "Starting Hour": hour,
                        "Finishing Hour": values[2],
                        "Assigned with": values[1]
                    })
