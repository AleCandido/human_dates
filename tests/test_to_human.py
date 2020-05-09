import datetime as dt

import pytest

import human_dates


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
