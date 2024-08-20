from sys import argv, exit
from pyfiglet import FigletFont, figlet_format


def main():
    # Determine if user passed 0 command-line arguments
    if len(argv) == 1:
        # Print user input with random font
        print_formatted("slant")

    elif len(argv) == 3:
        # Exit if user usage is not correct or font doesn't exist
        if (argv[1] != "-f" and argv[1] != "--font") or \
                    argv[2] not in FigletFont.getFonts():
            exit(f"Invalid usage")

        # Print user input with desired font
        print_formatted(argv[2])

    else:
        # Exit if user passes one or more than 2 command-line arguments
        exit("Invalid usage")


def print_formatted(fnt):
    # Get user input
    user_input = input("Input: ")

    # Select user font and print input
    f = figlet_format(user_input, font=fnt)
    print(f)


if __name__ == "__main__":
    main()
