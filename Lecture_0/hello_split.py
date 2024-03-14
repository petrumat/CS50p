# Ask user for input
name = input("What's your name? ")

# Remove leading and trailing special characters, digits, separators and symbols
name = name.strip(" 1234567890.,<>/?\\|;:\'\"[]{}-=_+*!@#$%^&()\t")

# Capitalize each word in name and 
# Split user's name into first name, middle name and last name
first, middle, last = name.title().split(maxsplit=2)

# Greet user by first name only
print(f"hello, {first}")