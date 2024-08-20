from random import randint


def main():
    # Get valid level from user
    level = get_level()

    # Generate math problems with that level
    math_problems(level)


def get_level():
    # Prompt until correct level value
    while True:
        level = input("Level: ")

        # If user input not numeric, prompt again
        if not level.isnumeric():
            continue
        else:
            # If user input not '1', '2' or '3', prompt again
            level = int(level)
            if level != 1 and level != 2 and level != 3:
                continue
            else:
                # Otherwise break loop and return user level
                break
    return level


def math_problems(level):
    # Start with score 0
    score = 0

    # Generate 10 math problems
    for _ in range(0, 10):
        # Generate two random number with level digits
        x = generate_integer(level)
        y = generate_integer(level)

        # Calculate correct result
        result = x + y

        # Prompt user to solve math problem (max 3 times)
        for attempt in range(0, 3):
            # Get user's answer
            answer = input(f"{x} + {y} = ")

            # If user input not numeric, prompt again
            if not answer.isnumeric():
                print("EEE")
                continue

            # Convert input to integer
            answer = int(answer)

            # If user input is not correct, prompt again
            if answer != result:
                print("EEE")
                continue

            # If user input is correct, terminate loop and update score
            else:
                score += 1
                break

        # If user still not correct after three tries, output solution
        if attempt == 2:
            print(f"{x} + {y} = {result}")

    # Print user's score
    print(score)


def generate_integer(level):
    # Raise ValueError if level is not '1', '2' or '3'
    if level < 1 or level > 3:
        raise ValueError

    # Generate number appropriately
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()
