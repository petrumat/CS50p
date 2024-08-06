def main():
    # Get message from user
    string = input("Greeting: ")

    print(greeting(string))


def greeting(string):
    # Remove spaces on left of input and treat case-insensitively
    string = string.strip(" ").lower()

    if string.find("h") == 0:
        if string.find("hello") == 0:
            return "$0"
        else:
            return "$20"
    return "$100"

if __name__ == "__main__":
    main()
