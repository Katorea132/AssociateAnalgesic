#!/usr/bin/python3
"""
This is the main module, used as a compass, it boths tells
which part and when each part should act.
"""

from magicdoer import assign_them_all, print_them_all, save_them_all

startups = {}
mentors = {}
assign_them_all(mentors, startups)
print_them_all(mentors)
save_them_all(mentors, startups)
