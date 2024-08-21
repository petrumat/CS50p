def main():
    # Get user word to shorten
    word = input("Input: ")

    # Eliminate vowels from word
    result = shorten(word)

    # Print resulting word
    print(result)


def shorten(word):
    # Check if word is str otherwise raise TypeError
    if type(word) is not str:
        raise TypeError

    # Define the possible vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # Look for all vowels and eliminate them
    for vowel in vowels:
        word = word.replace(vowel, "")

    # Return a str, not a list of str/chars
    return "".join(word)


if __name__ == "__main__":
    main()
