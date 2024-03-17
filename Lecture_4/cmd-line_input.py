from sys import argv

# ANSI color escape codes
class colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

class bright_colors:
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def main():
    print_prog_name()
    print_name()
    print_name_conditional()


def print_prog_name():
    prog_name = argv[0].lstrip('.\\')
    print(f"program name is {colors.GREEN}{prog_name}{colors.RESET}")


def print_name():
    try:
        print(f"hello, my name is {colors.CYAN}{argv[1]}{colors.RESET}.")
    except IndexError:
        print("Provide a name when running the program.")


def print_name_conditional():
    # Or interrogate the length of the command-line arguments list
    if len(argv) < 2:
        print("Too few arguments.")
    elif len(argv) > 2:
        print("Too many arguments.")
    else:
        print(f"hello, my name is {colors.CYAN}{argv[1]}{colors.RESET}.")


main()