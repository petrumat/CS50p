MAX_TRY = 3


def main():
    get_and_print_int_finally("x")
    read_and_print_int("y", "D:\\Documents\\CS50p\\Lecture_3\\input.txt")
    get_and_print_int_raise("z")


def get_and_print_int_finally(val_name):
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
            print(f"{val_name} is {n}")
            break
        finally:
            print("The 'try ... except' block worked")


def read_and_print_int(val_name, file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(f"{val_name} is {data}")
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")
    finally:
        print("Attempted to read the file.")


def get_and_print_int_raise(val_name):
    tries = 0
    while True:
        try:
            tries += 1
            n = int(input("What's the number? "))
        except ValueError:
            if tries < MAX_TRY:
                print(val_name, "is not an integer. Try again.")
            else:
                raise ValueError(f"{val_name} is not an integer after {MAX_TRY} attempts.")
        else:
            print(f"{val_name} is {n}")
            break
        finally:
            print("The 'try ... except' block worked")


main()