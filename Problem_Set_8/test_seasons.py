# Import necessary packages and modules
import pytest
from seasons import calculate_minutes, extract_from_date


# Test different (expected) combinations for calculate_minutes
def test_calculate_minutes_correct():
    assert calculate_minutes(2024, 8, 24) == 'Zero minutes'
    assert calculate_minutes(2024, 8, 23) == 'One thousand, four hundred forty minutes'
    assert calculate_minutes(2024, 7, 24) == 'Forty-four thousand, six hundred forty minutes'
    assert calculate_minutes(2023, 8, 24) == 'Five hundred twenty-seven thousand forty minutes'
    assert calculate_minutes(2022, 8, 24) == 'One million, fifty-two thousand, six hundred forty minutes'


# Test different (unexpected) combinations for calculate_minutes
def test_calculate_minutes_incorrect():
    with pytest.raises(SystemExit, match='Invalid date'):
        calculate_minutes(0000, 00, 00)
    with pytest.raises(SystemExit, match='Invalid date'):
        calculate_minutes(1970, 2, 31)


# Test invalid argument type for calculate_minutes
def test_calculate_minutes_invalid():
    with pytest.raises(TypeError):
        # Test argument type 'str'
        calculate_minutes('year', 'month', 'day')

        # Test argument type 'float'
        calculate_minutes(1970.0, 1.0, 1.0)


# Test different (expected) combinations for extract_from_date
def test_extract_from_date_correct():
    assert extract_from_date('0001-01-01') == (1, 1, 1)
    assert extract_from_date('0001-12-31') == (1, 12, 31)
    assert extract_from_date('1970-10-10') == (1970, 10, 10)
    assert extract_from_date('2024-08-24') == (2024, 8, 24)


# Test different (unexpected) combinations for extract_from_date
def test_extract_from_date_incorrect():
    with pytest.raises(SystemExit, match='Invalid date'):
        extract_from_date('January 1, 2000')
    with pytest.raises(SystemExit, match='Invalid date'):
        extract_from_date('0000-00-00')
    with pytest.raises(SystemExit, match='Invalid date'):
        extract_from_date('3000-13-40')


# Test invalid argument type for extract_from_date
def test_extract_from_date_invalid():
    with pytest.raises(TypeError):
        # Test argument type 'int'
        extract_from_date(10)

        # Test argument type 'float'
        extract_from_date(10.0)
