def main():
    # Get message from user
    time = input("What time is it? ")

    # Calculate time as float
    float_time = convert(time)
    if float_time == None:
        return

    # Show what to eat based on time
    print(output_message(float_time))


def convert(time):
    # Remove spaces on left and on right of input
    time = time.strip(" ")

    # Split input in *hours* and *minutes* components
    input = time.split(":", maxsplit=1)
    if len(input) != 2:
        return

    hours = float(input[0])

    #  Challenge
    if len(input[1]) == 7:
        # Determine day time or night time
        if input[1].endswith("a.m."):
            minutes = float(input[1].rstrip(" a.m."))
        else:
            hours += 12
            minutes = float(input[1].rstrip(" p.m."))
    elif len(input[1]) == 2:
        minutes = float(input[1])
    else:
        return

    # Validate time
    if hours < 0 or hours > 24 or minutes < 0 or minutes > 60:
        return

    # Calculate and return time as float
    minutes = minutes / 60
    return hours + minutes


def output_message(time):
    # Determine what to eat
    if 7 <= time <= 8:
        return "breakfast time"

    if 12 <= time <= 13:
        return "lunch time"

    if 18 <= time <= 19:
        return "dinner time"


if __name__ == "__main__":
    main()
