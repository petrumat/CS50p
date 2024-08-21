# Import math module to use modf
from math import modf


def main():
    # Get a valid fraction from user
    fraction = validate_input("Fraction: ")

    # Convert fraction to fuel level
    if fraction is not None:
        level = convert(fraction)

    # Show fuel gauge:
    print(gauge(level))


def validate_input(prompt):
    while True:
        # Get user input
        string = input(prompt).strip()

        # Determine if the user input contains "/" otherwise reject input
        if "/" not in string:
            continue

        # Split into two components
        first, second = string.split("/", maxsplit=1)

        try:
            # Try converting components into int and calculate result
            X = int(first)
            Y = int(second)

            # Determine if X <= Y otherwise reject input
            if X > Y:
                continue

            # Determine if Y is 0 and reject input
            if Y == 0:
                continue
        except ValueError:
            # If X or Y are not numbers reject input
            continue
        else:
            # Break while loop because the input is valid
            break

    return string


def convert(fraction):
    # Check if fraction is str otherwise raise TypeError
    if type(fraction) is not str:
        raise TypeError

    # Raise ValueError if fraction doesn't contains "/"
    if "/" not in fraction:
        raise ValueError

    # Split into two components
    X_str, Y_str = fraction.split("/", maxsplit=1)

    # Raise ValueError if X and/or Y is not integer
    if not X_str.isnumeric() or not Y_str.isnumeric():
        raise ValueError

    # Convert to type int
    X = int(X_str)
    Y = int(Y_str)

    # Raise ValueError if X and/or Y is negative or X > Y
    if X < 0 or Y < 0 or X > Y:
        raise ValueError

    # Raise ZeroDivisionError if Y is 0
    if Y == 0:
        raise ZeroDivisionError

    # Calculate and return rounded fuel level
    result = X / Y
    level_fractional, level_integer = modf(result * 100)
    if level_fractional >= 0.5:
        level_integer += 1

    return int(level_integer)


def gauge(percentage):
    # Check if fraction is str otherwise raise TypeError
    if type(percentage) is not int:
        raise TypeError

    # Return appropriate fuel level
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
