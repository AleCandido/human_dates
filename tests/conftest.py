import pytest

# define words used for pointing to past or future
class WordsTank:
    pass


past = WordsTank()
past.pre = ""
past.post = " ago"
# future
future = WordsTank()
future.pre = ""
future.post = " (future)"


@pytest.fixture
def templates():
    class Templates:
        pass

    ts = Templates()

    ts.past = f"{past.pre}%s{past.post}"
    ts.future = f"{future.pre}%s{future.post}"

    return ts
