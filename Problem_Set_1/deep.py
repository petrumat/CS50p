def main():
    # Get message from user
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    print(deep_thought(string))


def deep_thought(string):
    # Remove spaces on left and on right of input
    string = string.strip(" ")

    # Verify if input is a number
    if string.isnumeric():
        if int(string) == 42:
            return "Yes"
        else:
            return "No"
    else:
        string = string.lower()

        match string:
            case "forty-two" | "forty two":
                return "Yes"
            case _:
                return "No"


def deep_thought_easer(string):
    # Remove spaces on left of input and treat case-insensitively
    string = string.strip(" ").lower()

    match string:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"


if __name__ == "__main__":
    main()
