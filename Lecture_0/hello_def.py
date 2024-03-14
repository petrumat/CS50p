def main():
    # Get name from user
    name = input("What's your name? ")

    # Call function
    if(print_msg("hi,", name) != 0):
        return 1
    
    # Finish main function
    return 0


# Function to print message
def print_msg(msg="hello,", to="world"):
    print(f"{msg} {to}")
    return 0


main()