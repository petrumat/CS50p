from hello import hello


def test_hello_default():
    assert hello() == "hello, world"


def test_hello_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == "hello, " + name