def main():
    # Get name from user
    name = input("What's your name? ")

    # Call function with two positional arguments
    if(print_msg("hi,", name) != 0):
        return 1
    
    # Finish main function
    return 0


# Function to print message
def print_msg(msg="hello,", to="world"):
    # Str formatting method:
    print(f"{msg} {to}")

    # Str concatenation method:
    print(msg + " " + to)

    return 0


main()