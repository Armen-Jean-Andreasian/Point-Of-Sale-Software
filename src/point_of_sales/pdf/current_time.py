import time
from datetime import date


class Time:
    @staticmethod
    def current_time() -> str:
        ct_object = time.localtime(time.time())
        current_hour, current_minute, current_second = ct_object.tm_hour, ct_object.tm_min, ct_object.tm_sec
        formatted_time = f"{current_hour:02}:{current_minute:02}:{current_second:02}"
        return formatted_time

    @staticmethod
    def current_day() -> str:
        date_today = date.today().strftime('%Y-%m-%d')
        return date_today
