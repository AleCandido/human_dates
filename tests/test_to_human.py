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
        self.dates = [-dt.timedelta(hours=24.1), dt.timedelta(hours=24.5)]
        self.expected = ["yesterday", "tomorrow"]

    def test_time_hours(self):
        self.dates = [
            -dt.timedelta(hours=17.1),
            dt.timedelta(hours=5.1),
            -dt.timedelta(minutes=75),
        ]
        self.expected = [
            self.templates.past % "17 hours",
            self.templates.future % "5 hours",
            self.templates.past % "an hour",
        ]

    def test_time_minutes(self):
        self.dates = [
            -dt.timedelta(minutes=41.3),
            dt.timedelta(minutes=26.3),
            dt.timedelta(seconds=67),
        ]
        self.expected = [
            self.templates.past % "41 minutes",
            self.templates.future % "26 minutes",
            self.templates.future % "a minute",
        ]

    def test_time_seconds(self):
        self.dates = [-dt.timedelta(seconds=19.3), dt.timedelta(seconds=45.8)]
        self.expected = [
            self.templates.past % "19 seconds",
            self.templates.future % "45 seconds",
        ]

    def test_time_now(self):
        self.dates = [-dt.timedelta(seconds=3.7), dt.timedelta(seconds=8.1)]
        self.expected = ["just now"] * 2
