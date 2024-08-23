import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Raise error if argument is not type 'str'
    if type(s) is not str:
        raise TypeError

    # Correct pattern
    pattern = r'^<iframe[\w\s=":/\.;-]*src="https?://(www\.)?youtube\.com/embed/([^ ]+)"[\w\s=":/\.;-]*></iframe>$'

    # Try finding if str s matches pattern
    try:
        found = re.search(pattern, s)

        if found:
            # Extract substring after 'youtube.com/embed/'
            sub_str = found.group(2)

            # Prefix for found substring
            shorter = r'https://youtu.be/'

            # Return adjusted youtube URL
            return shorter + sub_str
        else:
            return None
    
    except AttributeError:
        # If s doesn't meet the pattern, just return 'None'
        return None


if __name__ == "__main__":
    main()
