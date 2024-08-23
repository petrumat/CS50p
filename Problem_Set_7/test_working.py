# Import necessary packages and modules
import pytest
from working import convert


# Test different (expected) str combinations
def test_str():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('5:00 PM to 9:00 AM') == '17:00 to 09:00'
    assert convert('10 AM to 8:50 PM') == '10:00 to 20:50'
    assert convert('10:30 PM to 8 AM') == '22:30 to 08:00'

# Test wrong hours
def test_wrong_str():
    with pytest.raises(ValueError):
        convert('')
    with pytest.raises(ValueError):
        convert('9AM')
    with pytest.raises(ValueError):
        convert('9 AM')
    with pytest.raises(ValueError):
        convert('9AM5PM')
    with pytest.raises(ValueError):
        convert('9AM 5PM')
    with pytest.raises(ValueError):
        convert('9 AM5 PM')
    with pytest.raises(ValueError):
        convert('9 AM 5 PM')
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00 PM')


# Test invalid argument type
# This won't pass check50 because of their implementation of 'working.py'
# def test_non_str():
#     with pytest.raises(TypeError):
#         convert(123)   # Test argument type 'int'
#         convert(123.567)   # Test argument type 'float'
