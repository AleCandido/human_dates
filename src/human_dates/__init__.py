# Core Imports
from datetime import datetime
from calendar import monthrange


# Initially taken unabashed from the following StackOverflow Post: http://stackoverflow.com/a/1551394/192791
def time_ago_in_words(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now

    second_diff = abs(diff.seconds)
    day_diff = diff.days
    if day_diff < 0:
        day_diff = -day_diff
        to = "f"
    else:
        to = "p"

    suffix = dict(f="(future)", p="ago")

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return str(second_diff) + f" seconds {suffix[to]}"
        if second_diff < 120:
            return f"a minute {suffix[to]}"
        if second_diff < 3600:
            return str(second_diff // 60) + f" minutes {suffix[to]}"
        if second_diff < 7200:
            return f"an hour {suffix[to]}"
        if second_diff < 86400:
            return str(second_diff // 3600) + f" hours {suffix[to]}"
    if day_diff == 1:
        return "yesterday" if to == "p" else "tomorrow"
    elif day_diff < 7:
        return f"{day_diff} days {suffix[to]}"
    elif day_diff < 31:
        w = int(day_diff // 7)
        return f"{w} weeks {suffix[to]}" if w > 1 else "a week {suffix[to]}"
    elif day_diff < 365:
        m = int(day_diff // 30)
        return f"{m} months {suffix[to]}" if m > 1 else "a month {suffix[to]}"
    else:
        y = int(day_diff // 365)
        return f"{y} years {suffix[to]}" if y > 1 else "a year {suffix[to]}"


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


def _parse_time_from_input(time=False):
    t = datetime.utcnow()
    if type(time) is int:
        t = datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        t = time
    return t
