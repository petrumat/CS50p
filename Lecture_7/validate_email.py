import re

def main():
    email = input("What's your email?").strip() # eliminate spaces in front and back
    # validate_re_rudimentary(email)
    validate_emali(email)
    
    
def validate_re_rudimentary(email):
    if re.search("@", email):
        print("Valid")
    else:
        print("Invalid")

    
def validate_emali(email):
    result = re.search(r"""
        ^(\w|\.)+               # one or more (ether one of (alphanumeric char or a ".")) at start of string
        @                       # one "@" char
        (\w+\.)+                # one or more (one or more alphanumeric chars and a ".")
        (com|edu|gov|net|org)$  # ether one of (com|edu|gov|net|org) at end of string
    """, email, re.IGNORECASE | re.VERBOSE)
    
    if result:
        print("Valid")
    else:
        print("Invalid")
    
    
if __name__ == "__main__":
    main()