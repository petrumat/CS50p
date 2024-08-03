def main():
    answer = input("Do you agree? ")

    print(compare(answer))
    print(compare_strip(answer))
    print(compare_lowercase(answer))
    print(compare_multiple(answer))
    print(compare_start(answer))


def compare(answer):
    # Compares strings

    if answer == "yes":
        return "Agreed"
    else:
        return "Not agreed"


def compare_strip(answer):
    # Strips string before comparing
    answer = answer.strip()

    if answer == "yes":
        return "Agreed"
    else:
        return "Not agreed"


def compare_lowercase(answer):
    # Lowercases string before comparing
    answer = answer.strip().lower()

    if answer == "yes":
        return "Agreed"
    else:
        return "Not agreed"
    

def compare_multiple(answer):
    # Compares multiple strings
    answer = answer.strip().lower()
    
    if answer == "yes" or answer == "y":
        return "Agreed"
    else:
        return "Not agreed"


def compare_start(answer):
    # Compares multiple strings
    answer = answer.strip().lower()

    if answer.startswith("y"):
        return "Agreed"
    else:
        return "Not agreed"
    

main()