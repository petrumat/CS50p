email = input("What's your email?").strip() # eliminate spaces in front and back

def main():
    # validate_chars()
    validate_username()


def validate_chars():
    if "@" in email and "." in email:
        print("Valid")
    else:
        print("Invalid")


def validate_username():
    username, domain = email.split("@")
    if username and domain.endswith(".com"):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()