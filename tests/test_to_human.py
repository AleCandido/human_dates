import datetime as dt

import pytest

import human_dates


class TestTimeAgoInWords:
    """
        test time_ago_in_words function
    """

    @pytest.fixture(autouse=True)
    def _import_templates(self, templates):
        """
            import templates from conftest local plugin
        """
        self.templates = templates

    @pytest.fixture(autouse=True)
    def _run_time_ago_comparison(self):
        """
            autoexecute after the specific test has been defined, running the
            actual comparison
        """
        yield
        for date, expected in zip(self.dates, self.expected):
            result = human_dates.time_ago_in_words(dt.datetime.now() + date)
            assert expected == result

    def test_time_years(self):
        self.dates = [-dt.timedelta(days=366 * 4), dt.timedelta(days=366 * 4)]
        self.expected = [
            self.templates.past % "4 years",
            self.templates.future % "4 years",
        ]

    def test_time_months(self):
        self.dates = [-dt.timedelta(days=31 * 3), dt.timedelta(days=31 * 3)]
        self.expected = [
            self.templates.past % "3 months",
            self.templates.future % "3 months",
        ]

    def test_time_weeks(self):
        self.dates = [-dt.timedelta(days=7 * 3 + 1), dt.timedelta(days=7 * 3 + 1)]
        self.expected = [
            self.templates.past % "3 weeks",
            self.templates.future % "3 weeks",
        ]

    def test_time_days(self):
        self.dates = [-dt.timedelta(days=5.1), dt.timedelta(days=5.1)]
        self.expected = [
            self.templates.past % "5 days",
            self.templates.future % "5 days",
        ]

    def test_time_one_day(self):
        self.dates = [-dt.timedelta(hours=25), dt.timedelta(hours=25)]
        self.expected = ["yesterday", "tomorrow"]
