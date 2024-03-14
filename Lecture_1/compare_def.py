def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    print(compare(x, y))
    print(compare_or(x, y))


def compare(x, y):
    if x < y:
        return "x is less than y"
    elif x > y:
        return "x is greater than y"
    else:
        return "x is equal to y"


def compare_or(x, y):
    if x < y or x > y:
        return "x is not equal to y"
    return "x is equal to y"


main()