# Import necessary packages and modules
import pytest
from plates import is_valid


# Test different str combinations for length
def test_str():
    assert is_valid('') == False
    assert is_valid('C') == False
    assert is_valid('CSC') == True
    assert is_valid('CSCS') == True
    assert is_valid('CSCSC') == True
    assert is_valid('CSCSCS') == True
    assert is_valid('CSCSCSC') == False

# Test plate starting with numbers
def test_start_number():
    assert is_valid('1CS50') == False

# Test plate with numbers in the middle
def test_middle_number():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
    assert is_valid('CS50P') == False
    assert is_valid('CS5050') == True

# Test plate with 0 first number used
def test_zero_first():
    assert is_valid('CS0') == False
    assert is_valid('CS05') == False
    assert is_valid('CS050P') == False

# Test plates with only numbers (type str)
def test_str_numbers():
    assert is_valid('123456') == False

# Test plates with only punctuation
def test_punctuation():
    assert is_valid('!@#$') == False
    assert is_valid('CS.50') == False

# Test is_valid argument type
def test_number():
    with pytest.raises(TypeError):
        # Test argument type 'int'
        is_valid(123)

        # Test argument type 'float'
        is_valid(123.567)
