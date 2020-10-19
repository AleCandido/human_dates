from .utils import _get_time_diff, _get_calendar_diff, _is_future

# Initially taken unabashed from the following StackOverflow Post:
# http://stackoverflow.com/a/1551394/192791
def time_ago_in_words(time):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc.
    
    If more `time` is more than one day far from `now`, then the 
    difference will take care only of dates (e.g.: ``time = 
    23:59 01/01/2020``, and ``now = 00:01 03/01/2020`` the result
    will be ``"two days ago"`` as well).
    """

    to = "f" if _is_future(time) else "p"
    if to == "p":
        diff = _get_time_diff(time)
    else:
        diff = _get_time_diff(None, time)

    second_diff = abs(diff.seconds)
    is_less_than_one_day = diff.days == 0

    suffix = dict(f="(future)", p="ago")

    if is_less_than_one_day:
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
    else:
        day_diff = abs(_get_calendar_diff(time).days)
        if day_diff == 1:
            return "yesterday" if to == "p" else "tomorrow"
        elif day_diff < 7:
            return f"{day_diff} days {suffix[to]}"
        elif day_diff < 31:
            w = int(day_diff // 7)
            return f"{w} weeks {suffix[to]}" if w > 1 else f"a week {suffix[to]}"
        elif day_diff < 365:
            m = int(day_diff // 30)
            return f"{m} months {suffix[to]}" if m > 1 else f"a month {suffix[to]}"
        else:
            y = int(day_diff // 365)
            return f"{y} years {suffix[to]}" if y > 1 else f"a year {suffix[to]}"


human_dates = hd = time_ago_in_words
