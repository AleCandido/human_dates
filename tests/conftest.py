import pytest


@pytest.fixture
def time_words():
    class TimeWords:
        pass

    tw, p, f = [TimeWords() for i in range(3)]
    # past
    p.pre = ""
    p.post = " ago"
    tw.past = p
    # future
    f.pre = ""
    f.post = " (future)"
    tw.future = f
    return tw
