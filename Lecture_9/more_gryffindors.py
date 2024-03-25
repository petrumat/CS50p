students = ["Hermione", "Harry", "Ron"]


def main():
    # print_gryffindors_rudimentary()
    # print_gryffindors_list_comprehension()
    # print_gryffindors_dict_comprehension()
    # print_students()
    print_ranking()


def print_gryffindors_rudimentary():
    print("Rudimentary:")

    gryffindors = []

    for student in students:
        gryffindors.append({"name": student, "house": "Gryffindor"})

    print(*gryffindors, sep="\n")


def print_gryffindors_list_comprehension():
    print("List Comprehension:")

    gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

    print(*gryffindors, sep="\n")


def print_gryffindors_dict_comprehension():
    print("Dictionary Comprehension:")

    gryffindors = {student: "Gryffindor" for student in students}

    print(gryffindors, sep="\n")


def print_students():
    for student in students:
        print(student)


def print_ranking():
    """Print rank and name the rudimentary way"""
    # for i in range(len(students)):
    #     print(i + 1, students[i])

    """Print rank and name the pythonic way (with enumerate)
    """
    for i, student in enumerate(students):
        print(i + 1, student)


if __name__ == "__main__":
    main()
