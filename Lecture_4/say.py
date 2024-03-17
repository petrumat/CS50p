import cowsay
from sys import argv, exit

def main():   
    if len(argv) == 1:
        print_all_characters()
    elif len(argv) == 2:
        character(argv[1], "Hello, there.")
    elif len(argv) == 3:
        character(argv[1], "Hello, " + argv[2] + ".")
    else:
        exit("Too many arguments.")


def print_all_characters():
    print("Available characters: ", end='')
    for character in cowsay.char_names:
        print(character, end=', ')


def character(char_name="cow", prompt="Hello, there."):
    try:
        print(cowsay.get_output_string(char_name, prompt), end='\n\n')
    except cowsay.CowsayError:
        print(argv[1] + " character non existent in cowsay module.\n")
        print_all_characters()


main()