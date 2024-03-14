# Set maximum number of tries
MAX_TRY = 3

# Ask user for input
name = input("What's your name? ")

# Check if name is a valid string
i = 1
while(True):
    if(i >= MAX_TRY):
        break

    # Check only for chars and not digits or separators.
    # This is a rudimentary method. More pythonic is to 
    # use lambda and regex input sanitation.
    if(not name.isalpha()):
        print("Name contains digits or separators. Try again.")
        name = input()
        i += 1
    else:
        break   # if input is correct to stop infinite loop

# Check if last name is correct or exit program with incorrect third input
if(not name.isalpha()):
    print("Name is invalid. Unsuccessfully tried 3 times.")
    exit()

# Capitalize name
name = name.capitalize()

# Greet user name
print(f"hello, {name}")