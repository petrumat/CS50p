# Import necessary packages and modules
import pytest
from fuel import convert, gauge


# Test different str combinations
def test_convert_str():
    assert convert('1/1000') == 0
    assert convert('1/4') == 25
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('1/1') == 100

# Test ValueError exception
def test_convert_ValueError():
    with pytest.raises(ValueError):
        # convert('')   # fails check50, but passes pytest (depends on check50's fuel.py)
        convert('/')    # missing X and Y
        convert('1/')   # missing Y
        convert('/1')   # missing X
        convert('1/cat')    # Y is str
        convert('cat/1')    # X is str
        convert('cat/dog')  # X and Y are str
        convert('2/1')  # X > Y
        convert('-1/')  # X is negative and missing Y
        convert('/-1')  # Y is negative and missing X
        convert('-1/cat')   # X is negative and Y is str
        convert('cat/-1')   # Y is negative and X is str
        convert('-2/-1')    # X and Y are negative and X < Y
        convert('-1/-4')    # X and Y are negative and X > Y

# Test ZeroDivisionError exception
def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('0/0')

# Test invalid argument type
# Fails check50, but passes pytest (depends on check50's fuel.py)
# def test_convert_number():
#     with pytest.raises(TypeError):
#         # Test argument type 'int' and 'float'
#         convert(50)
#         convert(33.33)

# Test different int combinations
def test_gauge_str():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(25) == '25%'
    assert gauge(50) == '50%'
    assert gauge(75) == '75%'

# Test invalid argument type
def test_gauge_invalid():
    with pytest.raises(TypeError):
        # Test argument type 'str' and 'float'
        gauge("50")
        gauge(33.33)
