def main():
    # Get message from user
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # Give answer to user
    print(deep_thought(string))

    # Optional easier function:
    # print(deep_thought_easer(string))


def deep_thought(string):
    # Remove spaces on left and on right of input
    string = string.strip(" ")

    # Verify if input is a number (over-engineered)
    if string.isnumeric():
        # Determine answer to give
        if int(string) == 42:
            return "Yes"
        else:
            return "No"
    else:
        string = string.lower()

        # Determine answer to give
        match string:
            case "forty-two" | "forty two":
                return "Yes"
            case _:
                return "No"


def deep_thought_easer(string):
    # Remove spaces on left of input and treat case-insensitively
    string = string.strip(" ").lower()

    # Determine answer to give
    match string:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


if __name__ == "__main__":
    main()
