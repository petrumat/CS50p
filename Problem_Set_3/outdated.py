# Dictionary with all possible months and corresponding numeric value
possible_months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

# Variable for printing debugging messages 
debugging = False


def main():
    date = get_valid_date("Date: ")
    print_date(date)


def get_valid_date(prompt):
    # Create empty date list containing year, month, day
    valid_date = []

    # Ask for input until valid input
    while True:
        # Get user input
        date = input(prompt).strip(" ")

        # Check date format
        if "/" in date:
            try:
                # Extract month, day, year components from date
                month, day, year = date.split("/", maxsplit=2)

                # This format supports only numeric months
                if not month.isnumeric():
                    continue

                # Validate user input
                if is_valid_date(month, day, year):
                    valid_date.append(year)
                    valid_date.append(month)
                    valid_date.append(day)
                    break
                else:
                    continue
            except ValueError:
                continue

        elif " " in date and "," in date:
            try:
                # Extract month, day, year components from date
                month, day, year = date.split(" ", maxsplit=2)

                # Eliminate trailing "," from day component
                day = day.rstrip(",")

                # Validate user input
                if is_valid_date(month, day, year):
                    valid_date.append(year)
                    valid_date.append(month)
                    valid_date.append(day)
                    break
                else:
                    continue
            except ValueError:
                continue
        else:
            continue

    # Return the valid date
    return valid_date


def is_valid_date(month, day, year):
    # Determine if month, day and year are valid
    valid_month = is_valid_month(month)
    valid_day = is_valid_day(day)
    valid_year = is_valid_year(year)

    # All date components must be valid
    return valid_month and valid_day and valid_year


def is_valid_month(month):
    # Month should be in possible_months list or between 1 and 12
    if month not in possible_months:
        if debugging:
            print(f"Month: {month} not in possible_months list")

        if not month.isnumeric():
            if debugging:
                print(f"Month: {month} not numeric")
            return False
        else:
            int_month = int(month)
            if int_month < 1 or int_month > 12:
                if debugging:
                    print(f"Month: {month} not between 1 and 12")
                return False
    return True


def is_valid_day(day):
    # Day should be between 1 and 31 (in this problem set)
    if not day.isnumeric():
        if debugging:
            print(f"Day: {day} not numeric")
        return False
    else:
        int_day = int(day)
        if int_day < 1 or int_day > 31:
            if debugging:
                print(f"Day: {day} not between 1 and 31")
            return False
    return True


def is_valid_year(year):
    # Year should be number
    if not year.isnumeric():
        if debugging:
            print(f"Year: {year} not numeric")
        return False
    return True


def print_date(date):
    # Extract year, month, day from date list
    year, month, day = date

    # Pad month with leading "0" if needed or convert numeric
    if month.isnumeric():
        formatted_month = month if len(month) == 2 else ("0" + month)
    else:
        formatted_month = possible_months[month]

    # Pad day with leading "0" if needed
    formatted_day = day if len(day) == 2 else ("0" + day)

    # Print desired date format
    print(f"{year}-{formatted_month}-{formatted_day}")


if __name__ == "__main__":
    main()
