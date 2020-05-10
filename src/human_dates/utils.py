from datetime import datetime
import numbers


def _parse_time_from_input(time, name=""):
    """
        parse time representation into a time object

        if time is None return :py:meth:`datetime.now`

        Parameters
        ----------
        time : number or datetime
            the time to be converted (if number it's considered a timestamp, see
            :py:meth:`datetime.timestamp`)

        Returns
        -------
        datetime.datetime
            the time object created
    """
    # __import__("pdb").set_trace()

    if time is None:
        return datetime.now()
    elif isinstance(time, numbers.Real):
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
            timestamp, see :py:meth:`datetime.timestamp`), if None use the
            current time
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

    time_end = _parse_time_from_input(time_end, "time_end")

    if time_beg > time_end:
        raise ValueError(
            "Times given in reversed order: time_end should be in the future of time_beg"
        )

    return time_end - time_beg


def _is_future(time, time_ref=None):
    """
        check if `time` is in future (w.r.t. `time_ref`, by default it is now)

        Parameters
        ----------
        time : int or datetime
            the time to check (if int it's considered a
            timestamp, see :py:meth:`datetime.timestamp`)
        time_ref : int or datetime
            the time reference (if int it's considered a timestamp, see
            :py:meth:`datetime.timestamp`), if None use the present time
            (default: None)

        Returns
        -------
        bool
            is in future or not

    """

    time = _parse_time_from_input(time, "time")

    if time_ref is None:
        time_ref = datetime.now()
    else:
        time_ref = _parse_time_from_input(time_ref, "time_ref")

    return time > time_ref


def _is_past(time, time_ref=None):
    """
        check if `time` is in past (w.r.t. `time_ref`, by default it is now)

        provided for convenience, is the opposite of :py:meth:`_is_future` by
        implementation (so same time means past, by convention).
    """

    return not _is_future(time, time_ref)
