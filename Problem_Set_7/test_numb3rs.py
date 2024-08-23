# Import necessary packages and modules
import pytest
from numb3rs import validate


# Test different (expected) str combinations
# Ideal str format: #.#.#.# ; where # is in [0, 255]
def test_str():
    assert validate('') == False    # Test empty argument
    assert validate('...') == False    # Test empty IP address
    assert validate('0.0.0.0') == True
    assert validate('1.0.0.0') == True
    assert validate('127.0.0.1') == True
    assert validate('255.0.0.0') == True
    assert validate('255.255.255.255') == True
    assert validate('256.255.255.255') == False
    assert validate('255.256.255.255') == False
    assert validate('255.255.256.255') == False
    assert validate('255.255.255.256') == False
    assert validate('255.512.512.512') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False


# Test invalid argument type
def test_non_str():
    with pytest.raises(TypeError):
        validate(123)   # Test argument type 'int'
        validate(123.567)   # Test argument type 'float'
