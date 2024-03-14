def main():
    x = int(input("What's the number? "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

    print(f"{x} is even") if is_even_pythonic(x) is True else print(f"{x} is odd")

    print(f"{x} is even") if is_even_better(x) is True else print(f"{x} is odd")


def is_even(n):
    if n % 2 == 0:
        return True
    return False


# The pythonic way to implement a conditional
def is_even_pythonic(n):
    return True if n % 2 == 0 else False


# Just return the result if itself is a boolean expression
def is_even_better(n):
    return n % 2 == 0


main()