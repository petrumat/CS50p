from random import randint


def main():
    # Get valid level from user
    level = get_level()

    # Start guessing game with that level
    guess_integer(level)


def get_level():
    # Prompt until correct level value
    while True:
        level = input("Level: ")

        # If user input not numeric, prompt again
        if not level.isnumeric():
            continue
        else:
            # If user input not positive integer, prompt again
            level = int(level)
            if level <= 0:
                continue
        # If all good, break infinite loop and return level
        break
    return level


def guess_integer(level):
    # Generate random number target
    target = randint(1, level)

    # Prompt until correct target value
    while True:
        number = input("Guess: ")

        # If user input not numeric, prompt again
        if not number.isnumeric():
            continue

        # Convert input to integer
        number = int(number)

        # If user input is smaller than target, prompt again
        if number < target:
            print(f"Too small!")
            continue

        # If user input is larger than target, prompt again
        elif number > target:
            print("Too large!")
            continue

         # If user input is target don't prompt again
        else:
            print("Just right!")

        # If numbered guessed, break infinite loop
        break


if __name__ == "__main__":
    main()
