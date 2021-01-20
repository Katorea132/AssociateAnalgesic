# Assoociate Analgesic


**Table of Contents**

[TOCM]

[TOC]

#What is this for:
Associate Analgesic is a program designed to automatize the assignation of meetings between mentors and startups, respecting the avaliable times for the mentors and avoiding collisions (meaning, a meeting with 2 startups at the same time in the side of a mentor or a startup having a meeting with 2 different mentors at the same time).

Such information is then displayed on a Console, as well as saved on a CSV file which can be easily imported to Google Sheets for easy visualization, the information in this CSV can be used to automate the scheduling on the calendars of both parties.

How to use it 
=============
You will need a CSV file in the same folder of the executable (or the script) called "data.csv", containing the pertinent data to do the matching, this must have the following characteristics
* As a CSV file, each field must be separated through commas
* The first row must be a row containing the headers, whatever name you decide to give to them is not important as long as the next instructions hold true for the followings rows
* The first field must contain the name of the mentor
* The second one must contain  which day of the week the mentor has avaliable, choosing exactly one of the following options: Monday, Tuesday, Wednesday, Thursday, Friday.
The program can be executed as a python script, for this you will need to install python 3 and execute the "main.py" file.
* The third one must peek a time frame, it can be either "AM"or "PM"
* Any other field will be considered a startup name and treated as so.


Run in the command line: python3 main.py
Or in its standalone version, by simply executing the program.
* The Ubuntu x86-64 version is called "Associate_Analgesic_ELFx86-64"
* The Windows 10 version is called "Associate_Analgesic.exe"
* There's no Mac version for I have no acces to such OS
* The windows version is recognized as a trojan by Windows Defender, thiswas made an standalone executable with pyinstaller with the following command "pyinstaller -F main.py", in case you want to reproducethe executable locally, even though it will most likely result in another False Positive.

Once it has been succesfully executed, a console will appear with the information of each mentor, with the assigned times for each start up.
* Those mentors that had undefined times avaliables didn't receive any for this information is not known yet
Also, multiple files will be created in CVS format, in order to be easily visualized through Google Sheets or similar tools.
The files generated will be
* "mentors_schedule.csv", the main CSV file, formatted to easily automate the calendar invitations
* Multiple CSV files called like each of the companies, these are useful in finding open spots in the schedules of each company to assign those mentors whose time is undefined at the moment in which the script is run
