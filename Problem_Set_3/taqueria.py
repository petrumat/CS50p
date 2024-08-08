# Felipe’s Taqueria menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    taqueria("Item: ")


def taqueria(prompt):
    # Begin with 0 total amount
    total_amount = 0

    # Ask for input until control-d
    while True:
        try:
            # Get user input
            item = input(prompt).title()

            # Check if item exists and calculate total amount
            if item not in menu:
                continue
            else:
                total_amount += menu[item]
                print(f"Total: ${total_amount:.2f}")
        except (KeyboardInterrupt, EOFError, KeyError):
            # Terminate function if exception raised
            print()
            return 0


if __name__ == "__main__":
    main()
