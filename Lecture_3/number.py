MAX_TRY = 3


def main():
    # get_and_print_int("x")

    # get_and_print_int_pass("x")

    x = get_int("What's the number?", "x is not an integer.")
    if x is not None:
        print(f"x is {x}")


def get_and_print_int(val_name):
    tries = 0
    while True:
        try:
            tries += 1
            n = int(input("What's the number? "))
        except ValueError:
            if tries < MAX_TRY:
                print(val_name, "is not an integer. Try again")
            else:
                print(val_name, "is not an integer.")
                print("Maximum tries to input a number exceed.")
                break
        else:
            print(f"x is {n}")
            break


def get_and_print_int_pass(val_name):
    while True:
        try:
            n = int(input("What's the number? "))
            print(f"{val_name} is {n}")
            return 0
        except ValueError:
            pass
            print("Not an integer.")


# This function will return None if no number is get received user
# after MAX_TRY times
def get_int(pos_prompt, neg_prompt):
    tries = 0
    while True:
        try:
            tries += 1
            return int(input(pos_prompt + " "))
        except ValueError:
            if tries < MAX_TRY:
                print(neg_prompt, "Try again.")
            else:
                print(neg_prompt, "Maximum tries to input a number exceed.")
                break


main()