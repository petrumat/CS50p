# Import necessary packages and modules
import pytest
from um import count


# Test different (expected) str combinations
def test_str():
    assert count('') == 0
    assert count('yum') == 0
    assert count('yummy') == 0
    assert count('um') == 1
    assert count('um?') == 1
    assert count('hello, um, world') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
    assert count('um, hello, um, world') == 2
    assert count('Um, I, um, count, um, four, um') == 4


# Test invalid argument type
def test_non_str():
    with pytest.raises(TypeError):
        count(123)   # Test argument type 'int'
        count(123.567)   # Test argument type 'float'
