import csv

students = []

def main():
    get_students()
    print_students()
    # print_sorted_students()
    # print_reverse_sorted_students()
    # print_sorted_students_by_home()
    # print_reverse_sorted_students_by_home()
    

def get_students():
    with open("students_homes.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "home": row[1]})
        # or knowing there are only 2 values in one row, do this:
        # for name, home in reader:
        #     students.append({"name": name, "home": home})


def print_students():
    print("Students' list:")
    for student in students:
        print(f"{student['name']} is from {student['home']}")


def print_sorted_students():
    print("Sorted students' list:")
    for student in sorted(students, key=lambda student: student["name"]):
        print(f"{student['name']} is from {student['home']}")


def print_reverse_sorted_students():
    print("Reverse sorted students' list:")
    for student in sorted(students, key=lambda student: student["name"], reverse=True):
        print(f"{student['name']} is from {student['home']}")


def print_sorted_students_by_home():
    print("Sorted students' list by home:")
    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student['name']} is in {student['home']}")


def print_reverse_sorted_students_by_home():
    print("Reverse sorted students' list by home:")
    for student in sorted(students, key=lambda student: student["home"], reverse=True):
        print(f"{student['name']} is in {student['home']}")


if __name__ == "__main__":
    main()