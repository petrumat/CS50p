def main():
    # Get message from user
    string = input("File name: ")

    print(extension(string))


def extension(string):
    # Remove spaces on left of input and treat case-insensitively
    string = string.rstrip(" ").lower()

    if string.endswith(".gif"):
        return "image/gif"
    elif string.endswith(".jpg") or string.endswith(".jpeg"):
        return "image/jpeg"
    elif string.endswith(".png"):
        return "image/png"
    elif string.endswith(".pdf"):
        return "application/pdf"
    elif string.endswith(".txt"):
        return "text/plain"
    elif string.endswith(".zip"):
        return "application/zip"

    return "application/octet-stream"


if __name__ == "__main__":
    main()
