def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove "$" from beginning of string
    dollars = d.lstrip("$")

    # Return dollars as float
    return float(dollars)


def percent_to_float(p):
    # Remove "%" from end of string
    percent = p.rstrip("%")

    # Return percent as float
    return float(percent)/100


if __name__ == "__main__":
    main()
