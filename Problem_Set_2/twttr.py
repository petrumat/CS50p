def main():
    user_input = input("Input: ")

    # Get a list of str/chars from remove_vowels()
    result = remove_vowels(user_input)

    # Print list without blank spaces
    print(*result, sep="")


def remove_vowels(user_input):
    # Define the possible vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # Look for all vowels and eliminate them
    for vowel in vowels:
        user_input = user_input.replace(vowel, "")

    return user_input


if __name__ == "__main__":
    main()
