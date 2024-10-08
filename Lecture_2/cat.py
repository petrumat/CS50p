def main():
    num_iterations = 3

    print_meow_3_times()
    # meow_while(num_iterations)
    # meow_for_constructor()
    # meow_for_list()
    # meow_for_range(num_iterations)
    # meow_for_pythonic(num_iterations)
    # meow_str(num_iterations)
    meow_user_iterations()


def print_meow_3_times():
    # Demonstrates multiple (identical) function calls
    print("meow")
    print("meow")
    print("meow")


def meow_while(n):
    # Demonstrates a while loop, counting up from 0 and more succinct incrementation. Introduces continue, break
    print("Using while statement:")
    
    i = 0
    while i < n:
        print(f"meow {i}")
        i += 1

        # An example on how to move to next iteration or escape loop
        if i < n:
            continue
        else:
            break
    
    print()


def meow_for_constructor():
    # Demonstrates a for loop, using a list
    print("Using for statement and list created by constructor:")
    first_list = list((1,2,3))  # Using a constructor to create a list
    for i in first_list:
        print(f"meow {i}")


def meow_for_list():
    # Demonstrates a for loop, using a list
    print("Using for statement and list created by assignment:")
    second_list = [1, 2, 3] # Creating a list by assigning values
    for i in second_list:
        print(f"meow {i}")


def meow_for_range(n):
    # Demonstrates a for loop, using range
    print("Using for statement and range:")
    for i in range(n):
        print(f"meow {i}")


def meow_for_pythonic(n):
    # Demonstrates a for loop, with _ as a variable
    print("Using for statement the pythonic way:")
    for _ in range(n):
        print("meow")


def meow_str(n):
    # Demonstrates str multiplication
    print("Using str concatenation:")
    print("meow\n" * n, end='')


def get_number():
    # Validates user input until a strictly positive number is given
    while True:
        n = int(input("How many times? "))

        if n > 0:
            return n
        

def meow_user_iterations():
    n = get_number()

    for _ in range(n):
        print("meow")


main()