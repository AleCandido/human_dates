from calendar import monthrange

from .utils import _parse_time_from_input


def beginning_of_year(time=False):
    time = _parse_time_from_input(time)
    return time.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)


at_beginning_of_year = beginning_of_year


def end_of_year(time=False):
    time = _parse_time_from_input(time)
    return time.replace(
        month=12, day=31, hour=23, minute=59, second=59, microsecond=999999
    )


at_end_of_year = end_of_year


def beginning_of_month(time=False):
    time = _parse_time_from_input(time)
    return time.replace(day=1, hour=0, minute=0, second=0, microsecond=0)


at_beginning_of_month = beginning_of_month


def end_of_month(time=False):
    time = _parse_time_from_input(time)
    days_in_month = monthrange(time.year, time.month)[1]
    return time.replace(
        day=days_in_month, hour=23, minute=59, second=59, microsecond=999999
    )


at_end_of_month = end_of_month


def beginning_of_day(time=False):
    time = _parse_time_from_input(time)
    return time.replace(hour=0, minute=0, second=0, microsecond=0)


midnight = beginning_of_day
at_midnight = beginning_of_day
at_beginning_of_day = beginning_of_day


def end_of_day(time=False):
    time = _parse_time_from_input(time)
    return time.replace(hour=23, minute=59, second=59, microsecond=999999)


at_end_of_day = end_of_day


def beginning_of_hour(time=False):
    time = _parse_time_from_input(time)
    return time.replace(minute=0, second=0, microsecond=0)


at_beginning_of_hour = beginning_of_hour


def end_of_hour(time=False):
    time = _parse_time_from_input(time)
    return time.replace(minute=59, second=59, microsecond=999999)


at_end_of_hour = end_of_hour


def beginning_of_minute(time=False):
    time = _parse_time_from_input(time)
    return time.replace(second=0, microsecond=0)


at_beginning_of_minute = beginning_of_minute


def end_of_minute(time=False):
    time = _parse_time_from_input(time)
    return time.replace(second=59, microsecond=999999)


at_end_of_minute = end_of_minute


def beginning_of_second(time=False):
    time = _parse_time_from_input(time)
    return time.replace(microsecond=0)


at_beginning_of_second = beginning_of_second


def end_of_second(time=False):
    time = _parse_time_from_input(time)
    return time.replace(microsecond=999999)


at_end_of_second = end_of_second
