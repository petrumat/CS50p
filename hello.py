# Printing just a string variable (with default new line at end) 
test_var = "This is just a test"
print(test_var)

# Printing a string variable without new line
print(test_var, end='') # Replaces new line ('\n') with nothing
print() # Adds just a new line

# Input string from user and prints it
name = input("What's your name? ")
print("hello, " + name) # Concatenating strings is one way to use print()
print("hello,", name, name)  # This is the simplest way to use print() -> adds ' ' (space) automatically between each arguments
print("hello,", name, name, sep='_')  # This is the simplest way to use print() -> adds specified separator ('_') between each arguments
print(f"hello, {name}") # This is the formatted way to use print()

# end=None => end='\n' and
# sep=None => sep=' ' (default values)