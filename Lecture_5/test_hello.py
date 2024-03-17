from hello import print_msg

def test_print_msg():
    assert print_msg("hello,", "world") == "hello, world"