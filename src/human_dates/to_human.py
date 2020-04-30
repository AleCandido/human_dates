from datetime import datetime

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
