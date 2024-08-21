# Import necessary modules
from sys import argv, exit


# main() expects one command-line argument (program name)
def main():
    # Exit if program call is incorrect
    if len(argv) < 2:
        exit(f"Too few command-line arguments")
    elif len(argv) > 2:
        exit(f"Too many command-line arguments")

    # Exit if program's name doesn't end in '.py'
    if not argv[1].endswith('.py'):
        exit(f"Not a Python file")

    # Show total lines of code
    print(count_lines(argv[1]))


def count_lines(file_name):
    # Reset counter
    line_counter = 0

    # Read whole file, line by line
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Exit if file doesn't exist
        exit(f"File does not exist")

    for line in lines:
        # Remove whitespaces
        line = line.lstrip(" \t")

        # Step over comments and blank lines
        if line.startswith("#") or line.startswith("\n"):
            continue

        # Update counter
        line_counter += 1

    return line_counter


if __name__ == "__main__":
    main()
