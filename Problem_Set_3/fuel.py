# Import math module to use modf
from math import modf

# Define maximum numbers of tries to get inputs
MAX_TRY = 10

def main():
    # Get a valid fraction from user
    fraction = valid_input("Fraction: ")

    # Show fuel gauge
    if fraction is not None:
        print(fuel_gauge(fraction))


def valid_input(prompt):
    tries = 0
    while True:
        # Determine if MAX_TRY is exceeded
        tries += 1
        if tries > MAX_TRY:
            # Terminate function because three consecutive inputs are invalid
            return None

        # Get user input
        string = input(prompt)

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

            result = X / Y
        except (ValueError, ZeroDivisionError):
            if tries > MAX_TRY:
                # Terminate function because three consecutive inputs are invalid
                return None
        else:
            # Break while loop because the input is valid
            break

    return result


def fuel_gauge(fraction):
    # Calculate fuel level
    fuel_level_fractional, fuel_level_integer = modf(fraction * 100)
    if fuel_level_fractional >= 0.5:
        fuel_level_integer += 1

    # Return appropriate fuel level
    if fuel_level_integer >= 99:
        return "F"
    elif fuel_level_integer <= 1:
        return "E"
    else:
        return f"{int(fuel_level_integer)}%"


if __name__ == "__main__":
    main()
