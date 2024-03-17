with open("names.txt", "r") as file:
    for line in file:
        # Eliminate '\n' from every line from file before print
        print("found", line.rstrip())