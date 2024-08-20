# Import emojize from emoji package
from emoji import emojize

def main():
    # Get user input with prompt
    user_input = input("Input: ")

    # Show converted input to emoji from full list and aliases
    print("Output:", emojize(user_input, language='alias'))


if __name__ == "__main__":
    main()
