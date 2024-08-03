def main():
    num_iterations = 3
    # print_row_str_multiplication(num_iterations)
    # print_row_for_loop(num_iterations)
    # print_columns(num_iterations)
    # print_square_nested_loops(num_iterations)
    print_square_pythonic(num_iterations)


def print_row_str_multiplication(n):
    # Prints a row of "n" bricks using str multiplication
    print("#" * n)


def print_row_for_loop(n):
    # Prints a row of "n" bricks using a for loop
    for _ in range(n):
        print("#", end='')
    print()


def print_columns(n):
    # Prints a column of "n" bricks using a loop
    for _ in range(n):
        print("#\n", end='')


def print_square_nested_loops(n):
    # Prints square of bricks using a function with nested loops
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()


def print_square_pythonic(n):
    # Prints square of bricks using a function with a loop and str multiplication
    for _ in range(n):
        print("#" * n)
        # or call print_row(n)


main()