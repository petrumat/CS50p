def main():
    # Get message from user
    time = input("What time is it? ")

    float_time = convert(time)
    if float_time == None:
        return

    print(output_message(float_time))


def convert(time):
    # Remove spaces on left and on right of input
    time = time.strip(" ")

    input = time.split(":", maxsplit=1)
    if len(input) != 2:
        return

    hours = float(input[0])

    #  Challenge
    if len(input[1]) == 7:
        if input[1].endswith("a.m."):
            minutes = float(input[1].rstrip(" a.m."))
        else:
            hours += 12
            minutes = float(input[1].rstrip(" p.m."))
    elif len(input[1]) == 2:
        minutes = float(input[1])
    else:
        return

    if hours < 0 or hours > 24 or minutes < 0 or minutes > 60:
        return

    minutes = minutes / 60

    return hours + minutes


def output_message(time):
    if 7 <= time <= 8:
        return "breakfast time"

    if 12 <= time <= 13:
        return "lunch time"

    if 18 <= time <= 19:
        return "dinner time"


if __name__ == "__main__":
    main()
