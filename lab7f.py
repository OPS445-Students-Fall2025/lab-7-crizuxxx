#!/usr/bin/env python3
# Student ID: ocoji

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__, __add__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """

    def __init__(self, hour=12, minute=0, second=0):
        """constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """return a string representation for print()"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """return a representation for interpreter (using dots)"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """return the result by using sum_times() method"""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify this Time object by adding seconds (can be + or -)."""
        current = self.time_to_sec()
        new = sec_to_time(current + seconds)
        self.hour, self.minute, self.second = new.hour, new.minute, new.second
        return None

    def time_to_sec(self):
        """convert object to seconds from midnight"""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def valid_time(self):
        """check if time object is valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True


def sec_to_time(seconds):
    """convert seconds to a Time object"""
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
