"""
Time: Utility class for working with time and date.

This module defines the Time class, which provides static methods for retrieving the current time
and date in specific formats.

Classes:
    Time: Utility class for working with time and date.

Methods:
    current_time: Get the current time in the format 'HH:MM:SS'.
    current_day: Get the current date in the format 'YYYY-MM-DD'.

Usage:
    The Time class is designed to provide easy access to the current time and date.
    You can use its static methods to retrieve the current time and date in specific formats.

Examples:
    # Get the current time
    current_time = Time.current_time()  # Returns a string like '18:21:39'

    # Get the current date
    current_date = Time.current_day()  # Returns a string like '2023-09-26'

Author:
    Your Name

"""


import time
from datetime import date


class Time:
    @staticmethod
    def current_time() -> str:
        """
        Get the current time in the format 'HH:MM:SS'.

        Returns:
            str: A string representing the current time.
        """
        ct_object = time.localtime(time.time())
        current_hour, current_minute, current_second = ct_object.tm_hour, ct_object.tm_min, ct_object.tm_sec
        formatted_time = f"{current_hour:02}:{current_minute:02}:{current_second:02}"
        return formatted_time

    @staticmethod
    def current_day() -> str:
        """
        Get the current date in the format 'YYYY-MM-DD'.

        Returns:
            str: A string representing the current date.
        """
        date_today = date.today().strftime('%Y-%m-%d')
        return date_today
