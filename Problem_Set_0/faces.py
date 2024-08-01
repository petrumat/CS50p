def main():
    # Get message from user
    string = input("What's the message? ")

    # Print updated massage
    print(convert(string))


def convert(str):
    # Replace ":)" with "🙂"
    str = str.replace(":)", "🙂")

    # Replace ":(" with "🙁"
    str = str.replace(":(", "🙁")

    # Return updated massage
    return str


if __name__ == "__main__":
    main()
