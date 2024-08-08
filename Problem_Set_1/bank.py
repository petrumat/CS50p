def main():
    # Get message from user
    string = input("Greeting: ")

    # Show amount owned
    print(greeting(string))


def greeting(string):
    # Remove spaces on left of input and treat case-insensitively
    string = string.strip(" ").lower()

    # Determine if str begins with an "h"
    if string.find("h") == 0:
        # Determine if str begins with a "hello"
        if string.find("hello") == 0:
            return "$0"
        else:
            return "$20"
    
    return "$100"

if __name__ == "__main__":
    main()
