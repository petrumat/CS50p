# Import necessary packages and modules
import pytest
from bank import value


# Test different (expected) str combinations
def test_str():
    # Test empty argument
    assert value('') == 100

    # Test lower case str
    assert value('hi') == 20

    # Test upper case str
    assert value('hello') == 0

    # Test upper case and lower case str
    assert value('Twitter') == 100

    # Test upper case str and numbers
    assert value('CS50') == 100

    # Test upper case, lower case, numbers and punctuation
    assert value('Hello, World. 50!') == 0


# Test different (unexpected) str combinations
def test_wired_str():
    # Test only numbers (type str)
    assert value('123') == 100

    # Test only punctuation
    assert value('!@#$$%^&*()') == 100


# Test invalid argument type
# This will fail in check50, but passes in pytest
def test_number():
    with pytest.raises(TypeError):
        # Test argument type 'int'
        value(123)

        # Test argument type 'float'
        value(123.567)
