from calculator import square
from sys import exit

def main():
    test_square(2, 4)
    test_square(3, 9)
    test_square(-2, 4)
    test_square(-3, 9)
    test_square(0, 0)


def test_square(n , val):
    try:
        assert square(n) == val
    except AssertionError:
        print(f"{n} squared is not {val}")


if __name__ == "__main__":
    main()