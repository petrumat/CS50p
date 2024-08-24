import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Raise error if argument is not type 'str'
    if type(s) is not str:
        raise TypeError

    # Correct pattern
    pattern = r'\b(um|Um|uM|UM)\b'

    # Try finding if s matches pattern
    result = re.findall(pattern, s)

    # Return number of pattern occurrences in s
    return len(result)


if __name__ == "__main__":
    main()
