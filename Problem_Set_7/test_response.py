# Import necessary packages and modules
import pytest
from response import is_valid_email


# Test different (expected) str combinations
def test_str():
    assert is_valid_email('') == False
    assert is_valid_email('malan') == False
    assert is_valid_email('malan@@@harvard.edu') == False
    assert is_valid_email('jhon.doe@github..com') == False
    assert is_valid_email('malan at harvard dot edu') == False
    assert is_valid_email('malan@harvard.edu') == True
    assert is_valid_email('jhon.doe@github.com') == True


# Test invalid argument type
def test_non_str():
    with pytest.raises(TypeError):
        is_valid_email(123)   # Test argument type 'int'
        is_valid_email(123.567)   # Test argument type 'float'
