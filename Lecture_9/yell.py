def main():
    # yell_message("This is CS50")
    # yell_rudimentary(["This", "is", "CS50"])
    # yell_uppercased(["This", "is", "CS50"])
    # yell_variable_number_of_arguments("This", "is", "CS50", "programming", "with", "Python")
    # yell_map("This", "is", "CS50")
    yell_list_comprehension("This", "is", "CS50")


def yell_message(message):
    print("yell_message():")
    print(message.upper())
    

def yell_rudimentary(words):
    print("yell_rudimentary():")
    for word in words:
        print(word.upper(), end=' ')
    print()


def yell_uppercased(words):
    print("yell_uppercased():")
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # print unpacked list


def yell_variable_number_of_arguments(*words):
    print("yell_variable_number_of_arguments():")
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)  # print unpacked list


def yell_map(*words):
    print("yell_map():")
    '''
    Map requires a function (this case str.upper without () because it
    is not called right away) and an iterable (this case a list with
    variable number of elements )
    '''
    uppercased = map(str.upper, words)
    print(*uppercased)


def yell_list_comprehension(*words):
    print("yell_list_comprehension():")
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()