# Import necessary modules
from sys import argv, exit
from csv import DictReader, writer


# main() expects two command-line argument (csv_read_from, csv_write_to)
def main():
    # Exit if program call is incorrect
    if len(argv) < 3:
        exit(f"Too few command-line arguments")
    elif len(argv) > 3:
        exit(f"Too many command-line arguments")

    # Exit if file's name doesn't end in '.csv'
    if not argv[1].endswith('.csv') or not argv[2].endswith('.csv'):
        exit(f"Both files must be CSV")

    # Read students' list
    students = read_students(argv[1])

    # Write updated students' list
    write_students(students, argv[2])


def read_students(file_name):
    # Start with empty list
    students = []

    # Try opening file to read
    try:
        with open(file_name, 'r') as file:
            # Create reader object
            reader_obj = DictReader(file)

            # Read whole file, line by line
            for row in reader_obj:
                students.append([row["name"], row["house"]])

    # Exit if file doesn't exist
    except FileNotFoundError:
        exit(f"Could not read {file_name}")

    # Return students' list
    return students


def write_students(students, file_name):
    # Create file to write
    with open(file_name, 'w', newline='' ) as file:
        # Create writer object
        writer_obj = writer(file)

        # Write header
        writer_obj.writerow(["first", "last", "house"])

        # Write in file, line by line
        for student_details in students:
            # Split student's name
            last, first = student_details[0].split(", ", maxsplit=1)

            # Write updated details
            writer_obj.writerow([first, last, student_details[1]])


if __name__ == "__main__":
    main()
