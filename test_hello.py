from hello import more_hello
from hello import more_goodbyes


def test_more_hello():
    assert "hi" == more_hello()


def test_more_hello2():
    assert "bye" == more_goodbyes()
