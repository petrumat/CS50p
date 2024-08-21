# Import necessary packages and modules
import pytest
from twttr import shorten


# Test different (expected) str combinations
def test_str():
    # Test empty argument
    assert shorten('') == ''

    # Test lower case str
    assert shorten('twitter') == 'twttr'

    # Test upper case str
    assert shorten('TWITTER') == 'TWTTR'

    # Test upper case and lower case str
    assert shorten('Twitter') == 'Twttr'

    # Test upper case str and numbers
    assert shorten('CS50') == 'CS50'

    # Test upper case, lower case, numbers and punctuation
    assert shorten('Hello, World. 50!') == 'Hll, Wrld. 50!'


# Test different (unexpected) str combinations
def test_wired_str():
    # Test only numbers (type str)
    assert shorten('123') == '123'

    # Test only punctuation
    assert shorten('!@#$$%^&*()') == '!@#$$%^&*()'


# Test invalid argument type
def test_number():
    with pytest.raises(TypeError):
        # Test argument type 'int'
        shorten(123)

        # Test argument type 'float'
        shorten(123.567)
