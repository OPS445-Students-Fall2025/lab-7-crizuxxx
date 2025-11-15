#!/usr/bin/env python3
# Student ID: ocoji

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second


def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'


def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total = Time(0, 0, 0)
    total.hour = t1.hour + t2.hour
    total.minute = t1.minute + t2.minute
    total.second = t1.second + t2.second

    # carry seconds -> minutes
    while total.second >= 60:
        total.second -= 60
        total.minute += 1

    # carry minutes -> hours
    while total.minute >= 60:
        total.minute -= 60
        total.hour += 1

    return total


def change_time(time, seconds):
    """Modify the given time object by adding 'seconds' (can be + or -)."""
    # add seconds directly
    time.second += seconds

    # handle overflow going forward
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    # handle underflow (negative seconds / minutes)
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    return None


def valid_time(t):
    """check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0
    """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True
