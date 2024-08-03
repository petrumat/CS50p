# Defines a global dict accessible in every function (after it)
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}


def main():
    # print("Hermione is in house " + students["Hermione"])
    print_students()
    print_students_pythonic()


def print_students():
    # Demonstrates indexing into a dict
    print(students["Hermione"])
    print(students["Harry"])
    print(students["Ron"])
    print(students["Draco"])


def print_students_pythonic():
    # Demonstrates iterating over and index into a dict
    for student in students:
        print(student, "is in house", students[student])


main()