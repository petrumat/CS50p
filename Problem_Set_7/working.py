import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Raise error if argument is not type 'str'
    if type(s) is not str:
        raise TypeError

    # Correct pattern
    pattern = r'^((0?[1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)) to ((0?[1-9]|1[0-2])(:[0-5][0-9])? (AM|PM))$'

    # Try finding if s matches pattern
    match = re.search(pattern, s)
    if match:
        first_time = match.group(1)     # First time before 'to'
        second_time = match.group(5)    # Second time after 'to'

        first = convert_time(first_time)
        second = convert_time(second_time)

        return first + ' to ' + second
    else:
        raise ValueError


def convert_time(time):
    # Pattern to extract time components
    pattern = r'^(0?[1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$'

    # Try finding if time matches pattern
    match = re.search(pattern, time)
    if match:
        # Extract components carefully:
        # Hours part needs to be prefixed by leading '0'
        # Minutes part can exist or not (e.g. '9 AM' returns 'None' for '00' minutes)
        hours = match.group(1) if len(match.group(1)) == 2 else '0' + match.group(1)
        minutes = match.group(2) if match.group(2) != None else ':00'
        meridiem = match.group(3)

        if meridiem == 'AM':
            # Adjust time if in interval [12:00 AM - 12:59 AM]
            return '00' + minutes if hours == '12' else hours + minutes
        else:
            if hours == '12':
                return hours + minutes
            else:
                # Adjust time if in interval [1:00 PM - 11:59 PM]
                int_hours = int(hours.lstrip('0')) + 12
                return str(int_hours) + minutes
    else:
        raise ValueError


if __name__ == "__main__":
    main()
