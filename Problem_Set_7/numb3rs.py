import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Raise error if argument is not type 'str'
    if type(ip) is not str:
        raise TypeError

    # Cover everything from "0.0.0.0" to "255.255.255.255"
    pattern = r'^(((1?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5]))\\.){3}((1?[0-9]?[0-9])|(2[0-4][0-9])|(25[0-5])){1}$'

    # Return True if ip matches pattern else False
    return False if re.match(pattern, ip) == None else True


if __name__ == "__main__":
    main()
