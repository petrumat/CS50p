def main():
    grocery_list = grocery()
    print_list(grocery_list)


def grocery():
    # Create empty dictionary
    grocery_list = {}

    # Ask for input until control-d
    while True:
        try:
            # Get user input
            item = input().upper()

            # Check if item exists and update total amount
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except (KeyboardInterrupt, EOFError, KeyError):
            # Terminate function if exception raised
            return grocery_list


def print_list(grocery_list):
    # Get item and value from the list in alphabetical order
    for item, value in sorted(grocery_list.items()):
        print(f"{value} {item}")


if __name__ == "__main__":
    main()