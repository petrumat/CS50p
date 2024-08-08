def main():
    variable_name = input("camelCase: ")

    # Get a list of str/chars from camel_case_to_snake_case()
    resulting_variable_name = camel_case_to_snake_case(variable_name)

    # Print list without blank spaces
    print(*resulting_variable_name, sep="")


def camel_case_to_snake_case(variable_name):
    # Create empty list for return
    resulting_variable_name = []

    # Iterate throw the input str
    i = 0
    while i < len(variable_name):
        # Change uppercase chars if needed
        if variable_name[i] >= "A" and variable_name[i] <= "Z":
            resulting_variable_name.append("_")
            resulting_variable_name.append(variable_name[i].lower())
        else:
            resulting_variable_name.append(variable_name[i])
        # Increment *i* for while loop
        i += 1

    return resulting_variable_name


if __name__ == "__main__":
    main()
