def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))

    print(compare(x, y))
    print(compare_or(x, y))
    print(compare_equal(x, y))
    print(compare_diff(x, y))
    print(compare_and(x))
    print(compare_and_better(x))
    print(compare_and_best(x))


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


def compare_equal(x, y):
    if x == y:
        return "x is equal to y"
    return "x is not equal to y"


def compare_diff(x, y):
    if x != y:
        return "x is different than y"
    return "x is the same as y"


def compare_and(x):
    if x < 10:
        return "x is less than 10"
    elif x >= 10 and x <= 100:
        return "x is between 10 and 100"
    elif x > 100 and x <= 1000:
        return "x is between 100 and 1000"
    return "x is greater than 1000"
    

def compare_and_better(x):
    if x < 10:
        return "x is less than 10"
    elif 10 <= x < 100:
        return "x is between 10 and 100"
    elif 100 <= x < 1000:
        return "x is between 100 and 1000"
    return "x is greater than 1000"


# The first satisfied if will exit the function, so the ifs actually
# compare score between last if value (eg. 100) and current if value (eg. 90)
def compare_and_best(score):
    if score > 100:
        return "score is to high"
    elif score >= 90:
        return "score is A"
    elif score >= 80:
        return "score is B"
    elif score >= 70:
        return "score is C"
    elif score >= 60:
        return "score is D"
    return "score is E"


main()