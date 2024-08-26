# Import necessary packages and modules
import pytest
from jar import Jar


def test_init():
    # Test default initialization
    jar1 = Jar()
    assert jar1.capacity == 12  # Default capacity
    assert jar1.size == 0    # No cookies initially

    # Test initialization with a custom capacity
    jar2 = Jar(20)
    assert jar2.capacity == 20  # Custom capacity
    assert jar2.size == 0    # No cookies initially

    # Test initialization with a negative capacity
    with pytest.raises(ValueError, match="Negative capacity"):
        _ = Jar(-5)  # This should raise a ValueError

    # Test initialization with a non-integer capacity
    with pytest.raises(TypeError, match="Wrong capacity type"):
        _ = Jar("large")  # type: ignore # This should raise a TypeError

    # Test initialization with no capacity provided
    with pytest.raises(ValueError, match="Missing capacity"):
        _ = Jar(None)  # type: ignore # This should raise a ValueError


def test_str():
    # Create Jar object with default capacity of cookies
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    # Create Jar object with default capacity of cookies
    jar = Jar()

    # Test depositing a valid number of cookies
    jar.deposit(5)
    assert jar.size == 5  # 5 cookies should be in the jar

    # Test depositing another valid number of cookies
    jar.deposit(3)
    assert jar.size == 8  # Now, 8 cookies should be in the jar

    # Test depositing too many cookies (exceeds capacity)
    with pytest.raises(ValueError, match="Too many cookies"):
        jar.deposit(10)  # This should raise a ValueError as 18 > 12 (capacity)

    # Test depositing a negative number of cookies
    with pytest.raises(ValueError, match="Wrong number"):
        jar.deposit(-1)  # This should raise a ValueError

    # Test depositing a non-integer value
    with pytest.raises(TypeError, match="Expected number"):
        jar.deposit("cookies")  # This should raise a TypeError


def test_withdraw():
    # Create Jar object with default capacity of cookies
    jar = Jar()
    jar.deposit(10)  # Start by depositing 10 cookies

    # Test withdrawing a valid number of cookies
    jar.withdraw(3)
    assert jar.size == 7  # 7 cookies should remain after withdrawing 3

    # Test withdrawing all remaining cookies
    jar.withdraw(7)
    assert jar.size == 0  # All cookies should be withdrawn

    # Test withdrawing more cookies than available
    with pytest.raises(ValueError, match="Too few cookies"):
        jar.withdraw(1)  # This should raise a ValueError as there are 0 cookies left

    # Test withdrawing a negative number of cookies
    with pytest.raises(ValueError, match="Wrong number"):
        jar.withdraw(-1)  # This should raise a ValueError

    # Test withdrawing a non-integer value
    with pytest.raises(TypeError, match="Expected number"):
        jar.withdraw("cookies")  # This should raise a TypeError


def test_capacity_getter():
    # Create Jar object with a valid capacity of cookies
    jar1 = Jar(20)
    assert jar1.capacity == 20

    # Create Jar object with default capacity of cookies
    jar2 = Jar()
    # Capacity should be default value
    assert jar2.capacity == 12


def test_capacity_setter():
    # capacity is a property and not a method
    # The correct way to set the property value is by assigning a value directly

    # Create Jar object
    jar = Jar()

    with pytest.raises(TypeError, match='Wrong capacity type'):
        jar.capacity = "123"     # Test argument type 'str'
        jar.capacity = 123.567   # Test argument type 'float'

    with pytest.raises(ValueError, match='Negative capacity'):
        jar.capacity = -12
        jar.capacity = -100

    with pytest.raises(ValueError, match='Missing capacity'):
        jar.capacity = None
