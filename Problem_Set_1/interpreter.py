def main():
    # Get message from user
    string = input("Expression: ")

    print(math_interpreter(string))


def math_interpreter(string):
    # Remove spaces on left and on right of input
    string = string.strip(" ")

    input = string.split(" ", maxsplit=2)
    if len(input) != 3:
        return "Exactly 3 arguments required"

    if input[0].isnumeric():
        x = float(input[0])
    else:
         return "NaN"

    if input[2].isnumeric():
        z = float(input[2])
    else:
        return "NaN"

    match input[1]:
        case "+":
            return f"{(x + z):.1f}"
        case "-":
            return f"{(x - z):.1f}"
        case "*":
            return f"{(x * z):.1f}"
        case "/":
            return f"{(x / z):.1f}"
        case _:
            return "NaN"


if __name__ == "__main__":
    main()
