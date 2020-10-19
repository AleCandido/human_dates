import datetime as dt
import itertools

import pytest

import human_dates


class TestUtils:
    timestamps = [213, 391.1234, 2198348, 14, 1e7]

    def test_input_parser(self):
        datetimes = [dt.datetime.fromtimestamp(ts) for ts in self.timestamps]

        # check timestamps conversion
        assert all(
            [
                human_dates.utils._parse_time_from_input(ts) == dt
                for ts, dt in zip(self.timestamps, datetimes)
            ]
        )

        # check datetimes untouched
        assert all(
            [human_dates.utils._parse_time_from_input(dt) == dt for dt in datetimes]
        )

    def test_input_parser_failures(self):
        # not all numeric numbers are accepted
        import decimal

        with pytest.raises(ValueError, match=".*not recognised.*"):
            human_dates.utils._parse_time_from_input(
                decimal.Decimal(self.timestamps[0])
            )

        # not accept string representations
        with pytest.raises(ValueError, match=".*not recognised.*"):
            human_dates.utils._parse_time_from_input("05/09/2020, 12:52:19")

    def test_time_diff(self):
        for x, y in itertools.product(self.timestamps, self.timestamps):
            if y >= x:
                assert human_dates.utils._get_time_diff(x, y) == dt.timedelta(
                    seconds=(y - x)
                )
            else:
                # expected failure if dates are in reversed order
                with pytest.raises(ValueError, match=".*reversed.*future.*"):
                    assert human_dates.utils._get_time_diff(x, y) == dt.timedelta(
                        seconds=(y - x)
                    )

    def test_calendar_diff(self):
        for x, y in itertools.product(self.timestamps, self.timestamps):
            diff = human_dates.utils._get_calendar_diff(x, y).days
            assert abs(diff) <= abs(dt.timedelta(seconds=(y - x)).days)
            if x >= y:
                diff <= 0

    def test_in_future(self):
        for x, y in itertools.product(self.timestamps, self.timestamps):
            if y > x:
                assert human_dates.utils._is_future(y, x)

    def test_in_past(self):
        for x, y in itertools.product(self.timestamps, self.timestamps):
            assert human_dates.utils._is_past(x, y) != human_dates.utils._is_future(
                x, y
            )
