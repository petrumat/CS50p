def main():
    name = input("What's your name? ")
    print_msg("hi,", name)


def print_msg(msg="hello,", to="world"):
    print(f"{msg} {to}")


if __name__ == "__main__":
    main()