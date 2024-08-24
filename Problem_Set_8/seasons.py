from datetime import date
import sys, re, inflect


def main():
    birth_date = input("Date of Birth: ")

    year, month, day = extract_from_date(birth_date)

    print(calculate_minutes(year, month, day))


def extract_from_date(birth_date):
    # Raise error if argument is not type 'str'
    if type(birth_date) is not str:
        raise TypeError

    # Basic regex pattern to validate and extract date components
    pattern = r'^([0-2][0-9][0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$'

    # Try finding if birth_date matches pattern
    match = re.search(pattern, birth_date)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)

        # If any date component is missing, terminate program
        if year == None or month == None or day == None:
            sys.exit("Invalid date")

        # Return date component as integers
        return int(year), int(month), int(day)
    
    else:
        # If birth_date doesn't match pattern, terminate program
        sys.exit("Invalid date")


def calculate_minutes(year, month, day):
    # Raise error if any argument is not type 'int'
    if type(year) is not int or type(month) is not int or type(day) is not int:
        raise TypeError

    # Try converting arguments in datetime.date
    try:
        birth_date = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")

    # Determine current date and how many days have past since birth_date
    current_date = date.today()
    timedelta = current_date - birth_date
    days = timedelta.days

    # Calculate minutes
    minutes = days * 24 * 60

    # Convert numerals to words using inflect package
    inflect_eng = inflect.engine()
    words = inflect_eng.number_to_words(minutes, andword="") # type: ignore

    # Return in desired format
    return words.capitalize() + ' minutes' # type: ignore


if __name__ == "__main__":
    main()
