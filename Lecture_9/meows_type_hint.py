def main():
    number: int = int(input("Number: "))

    # print("Calls meow() function:")
    # meow(number)
    
    # print("Calls meow() function and prints return value:")
    # ''' assumes that meow() returns a string object'''
    # meows: str = meow(number)
    # print(meows)
    
    print("Calls return_meow() function and prints return value:")
    meows: str = return_meow(number)
    print(meows)


def meow(n: int) -> None:
    for _ in range(n):
        print("meow")


def return_meow(n: int) -> str:
    """Meow n times"""    # typical pythonic comment
    
    """
    Meow n times
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """     # typical pythonic comment for more complex functions
    return "meow\n" * n


if __name__ == "__main__":
    main()