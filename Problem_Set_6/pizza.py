# Import necessary modules
from sys import argv, exit
from tabulate import tabulate
from csv import DictReader


# main() expects one command-line argument (csv file name)
def main():
    # Exit if program call is incorrect
    if len(argv) < 2:
        exit(f"Too few command-line arguments")
    elif len(argv) > 2:
        exit(f"Too many command-line arguments")

    # Exit if file's name doesn't end in '.csv'
    if not argv[1].endswith('.csv'):
        exit(f"Not a CSV file")

    # Read menu and header from '.csv' file
    menu, header = get_menu(argv[1])

    # Show menu in table form
    print(tabulate(menu, header, tablefmt="grid"))


def get_menu(file_name):
    # Start with empty menu
    menu = []

    # Determine first element in header based on file's name
    pizza_type = file_name.removeprefix(".\\").removesuffix(".csv").capitalize()
    pizza = pizza_type + " Pizza"
    header = [pizza, "Small", "Large"]

    # Read whole file, line by line
    try:
        with open(file_name) as file:
            reader = DictReader(file)
            for row in reader:
                menu.append([row[pizza], row["Small"], row["Large"]])
    except FileNotFoundError:
        # Exit if file doesn't exist
        exit(f"File does not exist")

    # Return both menu and header
    return menu, header


if __name__ == "__main__":
    main()
