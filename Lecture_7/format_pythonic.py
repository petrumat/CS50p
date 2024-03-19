import re

def main():
    name = input("What's your name?").strip() # eliminate spaces in front and back
    
    if matches := re.search(r"^(.+), *(.+)$", name):
        name = matches.group(2) + " " + matches.group(1)
    
    print(name)


if __name__ == "__main__":
    main()