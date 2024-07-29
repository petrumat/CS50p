def main():
    print(f"1+2={one_plus_two()}")

    # division()

    # concat_strings()

    # str_to_int()

    # function_nesting()

    # round_sum()
    # round_sum_fewer_var()

    # format_max_zero()

    # format_decimals()


def one_plus_two():
    # Demonstrates addition and defining a function with a return value

    x = 1
    y = 2

    z = x + y

    return z


def division():
    # Demonstrates division

    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = x / y

    print(z)


def square(a = 0.0):
    # Demonstrates squaring:

    a **= 2
    return a

    '''
        Other methods are:
        return a * a
        return a ** 2
        return pow(a, 2)
    '''


def concat_strings():
    # Demonstrates (unintended) concatenation of strings

    # Prompt user for two integers
    x = input("What's x? ")
    y = input("What's y? ")

    # Print sum
    z = x + y
    print(z)


def str_to_int():
    # Demonstrates conversion from str to int

    x = input("What's x? ")
    y = input("What's y? ")

    z = int(x) + int(y)

    print(z)

    # Demonstrates conversion from str to float
    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = x + y

    print(z)


def function_nesting():
    # Demonstrates nesting of function calls

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    z = x + y

    print(z)


def round_sum():
    # Demonstrates rounding to nearest int

    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = round(x + y)

    print(z)


def round_sum_fewer_var():
    # Demonstrates round_sum() with fewer variables

    x = float(input("What's x? "))
    y = float(input("What's y? "))

    print(round(x + y))


def format_max_zero():
    # Formats result to max 10 decimals with no unnecessary 0 decimals.

    x = float(input("What's x? "))
    
    print(f"x={x:,.10g} squared is {square(x):,.10g}")


def format_commas():
    # Demonstrates formatting with commas

    x = float(input("What's x? "))
    y = float(input("What's y? "))

    z = round(x + y)

    print(f"{z:,}")


def format_decimals():
    # Demonstrates formatting after the decimal place

    x = int(input("What's x? "))
    y = int(input("What's y? "))

    z = x / y

    print(f"{z:.2f}")


main()