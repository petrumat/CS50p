from hello import hello


def test_hello_default():
    assert hello() == "hello, world"


def test_hello_argument():
    assert hello("David") == "hello, David"