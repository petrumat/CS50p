def main():
    # Get message from user
    string = input("What's the message? ")

    # Replace space with "..."
    string = string.replace(" ", "...")

    # Print updated massage
    print(string)


if __name__ == "__main__":
    main()
