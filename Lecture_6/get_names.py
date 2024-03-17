with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    # Eliminate '\n' from every line from file before print
    print("found", line.rstrip())