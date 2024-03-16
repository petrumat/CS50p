students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}


def main():
    # print("Hermione is in house " + students["Hermione"])
    print_students()

def print_students():
    for student in students:
        print(student, "is in house", students[student])


main()