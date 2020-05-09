from datetime import datetime


def _parse_time_from_input(time, name=""):
    """
        parse time representation into a time object

        Parameters
        ----------
        time : int or datetime
            the time to be converted (if int it's considered a timestamp, see
            :py:meth:`datetime.timestamp`)

        Returns
        -------
        datetime.datetime
            the time object created
    """
    if type(time) is int:
        return datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        return time
    else:
        name = name + " " if name else ""
        msg = "%stype not recognised: not a known time representation"
        raise ValueError(msg % name)


def _get_time_diff(time_beg, time_end=None):
    """
        get the difference of two objects representing times (as a time)

        Parameters
        ----------
        time_beg : int or datetime
            the beginning of the time interval (if int it's considered a
            timestamp, see :py:meth:`datetime.timestamp`)
        time_end : int or datetime
            the end of the time interval (if int it's considered a timestamp, see
            :py:meth:`datetime.timestamp`), if None use the current time
            (default: None)

        Returns
        -------
        datetime.timedelta
            the difference as a time interval

    """

    time_beg = _parse_time_from_input(time_beg, "time_beg")

    if time_end is None:
        time_end = datetime.utcnow()
    else:
        time_end = _parse_time_from_input(time_end, "time_end")

    return time_end - time_beg
