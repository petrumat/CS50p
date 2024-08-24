from validator_collection import checkers


def main():
    # Show 'Valid' or 'Invalid'
    print("Valid" if is_valid_email(input("What's your email address? ")) else "Invalid")


def is_valid_email(email):
    if type(email) != str:
        raise TypeError

    # Returns checkers.is_email() response of True or False
    return checkers.is_email(email)


if __name__ == "__main__":
    main()
