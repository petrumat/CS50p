# Set maximum number of tries
MAX_TRY = 3

# Ask user for input
name = input("What's your name? ")

# Remove leading and trailing special characters, digits, separators and symbols
name = name.strip(" 1234567890.,<>/?\\|;:\'\"[]{}-=_+*!@#$%^&()\t")

# Capitalize name
name = name.capitalize()

# Greet user name
print(f"hello, {name}")