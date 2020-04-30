import datetime as dt

import pytest

import human_dates


class TestBeginningOf:
    def test_beginning_of_year(self):
        date = dt.datetime.strptime("Jun 13 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime("Jan 1 2005  12:00AM", "%b %d %Y %I:%M%p")
        result = human_dates.beginning_of_year(date)
        assert expected == result

    def test_beginning_of_month(self):
        date = dt.datetime.strptime("Jun 13 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime("Jun 1 2005  12:00AM", "%b %d %Y %I:%M%p")
        result = human_dates.beginning_of_month(date)
        assert expected == result

    def test_beginning_of_day(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime("Jun 1 2005  12:00AM", "%b %d %Y %I:%M%p")
        result = human_dates.beginning_of_day(date)
        assert expected == result

    def test_beginning_of_hour(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime("Jun 1 2005  1:00PM", "%b %d %Y %I:%M%p")
        result = human_dates.beginning_of_hour(date)
        assert expected == result

    def test_beginning_of_minute(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33.123456PM", "%b %d %Y %I:%M.%f%p")
        expected = dt.datetime.strptime("Jun 1 2005  1:33PM", "%b %d %Y %I:%M%p")
        result = human_dates.beginning_of_minute(date)
        assert expected == result


class TestEndOf:
    def test_end_of_year(self):
        date = dt.datetime.strptime("Jun 13 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime(
            "Dec 31 2005  23:59:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_year(date)
        assert expected == result

    def test_end_of_month(self):
        date = dt.datetime.strptime("Feb 13 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime(
            "Feb 28 2005  23:59:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_month(date)
        assert expected == result

    def test_end_of_month_leapyear(self):
        date = dt.datetime.strptime("Feb 13 2008  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime(
            "Feb 29 2008  23:59:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_month(date)
        assert expected == result

    def test_end_of_day(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime(
            "Jun 1 2005  23:59:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_day(date)
        assert expected == result

    def test_end_of_hour(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33PM", "%b %d %Y %I:%M%p")
        expected = dt.datetime.strptime(
            "Jun 1 2005  13:59:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_hour(date)
        assert expected == result

    def test_end_of_minute(self):
        date = dt.datetime.strptime("Jun 1 2005  1:33.123456PM", "%b %d %Y %I:%M.%f%p")
        expected = dt.datetime.strptime(
            "Jun 1 2005  13:33:59.999999", "%b %d %Y %H:%M:%S.%f"
        )
        result = human_dates.end_of_minute(date)
        assert expected == result


class TestTimeAgoInWords:
    def test_time_years(self, time_words):
        date = dt.datetime.now() - dt.timedelta(days=366 * 4)
        expected = f"{time_words.past.pre}4 years{time_words.past.post}"
        result = human_dates.time_ago_in_words(date)
        assert expected == result

    def test_time_weeks(self, time_words):
        date = dt.datetime.now() - dt.timedelta(days=7 * 3 + 1)
        expected = f"{time_words.past.pre}3 weeks{time_words.past.post}"
        result = human_dates.time_ago_in_words(date)
        assert expected == result

    def test_time_years_future(self, time_words):
        date = dt.datetime.now() + dt.timedelta(days=366 * 4)
        expected = f"{time_words.future.pre}4 years{time_words.future.post}"
        result = human_dates.time_ago_in_words(date)
        assert expected == result

    def test_time_weeks_future(self, time_words):
        date = dt.datetime.now() + dt.timedelta(days=7 * 3 + 1)
        expected = f"{time_words.future.pre}3 weeks{time_words.future.post}"
        result = human_dates.time_ago_in_words(date)
        assert expected == result
