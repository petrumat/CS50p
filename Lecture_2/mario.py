def main():
    num_iterations = 3
    # print_row(num_iterations)
    # print_columns(num_iterations)
    print_square(num_iterations)


def print_row(n):
    # print("#" * n)    # or use a for loop

    for _ in range(n):
        print("#", end='')
    print()


def print_columns(n):
    for _ in range(n):
        print("#\n", end='')


def print_square(n):
    for _ in range(n):
        print("#" * n)  # or call print_row(n)
        # print_row(n)


main()