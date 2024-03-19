import re

def main():
    name = input("What's your name?").strip() # eliminate spaces in front and back
    
    matches = re.search(r"^(.+), *(.+)$", name)
    
    # Explinations:
    # matches = re.search(r"""
    #     ^(.+)       # one or more chars at start of string
    #     , *         # one "," char and zero or more " " char
    #     (.+)&       # one or more chars at end of string
    # """, name)

    # if matches:
    #     last, first = matches.groups()
    #     name = f"{first} {last}"
    # Or even simpler:
    if matches:
        name = matches.group(2) + " " + matches.group(1)
    
    print(name)


if __name__ == "__main__":
    main()