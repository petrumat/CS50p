# import random
from random import choice, randint, shuffle

def main():
    # flip_coin()
    # print(generate_number(1, 10))
    shuffle_list(9)


def flip_coin():
    coin = choice(["heads", "tails"])
    print(f"Face of the coin is {coin}.")


def generate_number(min, max):
    return randint(min, max)


def shuffle_list(last_element):
    # Generate list of int from 0 to last_element
    my_list = list(range(last_element + 1))
    shuffle(my_list)
    print(my_list)
    return 0


main()