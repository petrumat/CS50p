def main():
    # Get message from user
    greeting = input("Greeting: ")

    # Show amount of $
    print(f"$ {value(greeting)}")


def value(greeting):
    # Raise error if argument is not type 'str'
    if type(greeting) is not str:
        raise TypeError

    # Remove spaces on left of input and treat case-insensitively
    greeting = greeting.strip(" ").lower()

    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            # Starts with 'hello'
            return 0
        else:
            # Starts with 'h'
            return 20
    # Starts with anything but 'h'
    return 100

if __name__ == "__main__":
    main()
