import inflect


def main():
    # Create empty names list
    names = []

    # Create inflect engine
    inflect_eng = inflect.engine()

    # Ask for input until control-d
    while True:
        try:
            # Get user input
            name = input("Name: ").rstrip()

            # Add name in names list
            names.append(name)

        except (KeyboardInterrupt, EOFError, KeyError):
            # Update names list with commas and one 'and' as needed
            updated_names = inflect_eng.join(names)

            # Print names on new line
            print(f"\nAdieu, adieu, to {updated_names}")

            # Return code 0 as exception was handled
            return 0


if __name__ == "__main__":
    main()
