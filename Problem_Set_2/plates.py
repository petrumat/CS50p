import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # User str is valid if it meets all requirements
    return (starts_with_two_letters(s)
            and has_required_length(s)
            and no_numbers_inside(s)
            and no_punctuation(s))


def starts_with_two_letters(s):
    # Determine if s has at least two chars
    if len(s) < 2:
        return False

    # Define all possible uppercase letters
    uppercase_letters = list(string.ascii_uppercase)

    # Determine if first two chars are letters
    return s[0] in uppercase_letters and s[1] in uppercase_letters


def has_required_length(s):
    # Determine if length of s is between 2 and 6
    return len(s) >= 2 and len(s) <= 6


def no_numbers_inside(s):
    # Define all possible digits
    digits = list(string.digits)

    digit_chars_after_first_digit = True
    first_digit_not_zero = False

    # Determine if plate has digits
    has_digits = False
    first_digit_index = 0
    for char in s:
        if char in digits:
            # Find first digit's index and break loop to save runtime
            has_digits = True
            first_digit_index = s.find(char)
            break

    if has_digits:
        # Determine if all chars after first digit are digits
        for char in s[first_digit_index:]:
            if char not in digits:
                digit_chars_after_first_digit = False

        # Determine if first digit is not zero
        if "0" not in s:
            first_digit_not_zero = True
        else:
            zero_index = s.find("0")
            # Determine if first three chars are "0"
            if zero_index < 3:
                return False
            # Determine if char before index is a digit
            if s[zero_index-1] in digits:
                first_digit_not_zero = True
        return digit_chars_after_first_digit and first_digit_not_zero
    else:
        # Plate doesn't have digits at all
        return True


def no_punctuation(s):
    # Define all possible punctuation chars
    punctuations = list(string.punctuation)
    punctuations.append(" ")

    # Determine if plate has punctuation
    has_punctuation = False
    for char in s:
        if char in punctuations:
            # Find first punctuation and break loop to save runtime
            has_punctuation = True
            break

    return not has_punctuation


main()
