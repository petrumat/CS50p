students = ["Hermione", "Harry", "Ron", "Draco"]


def main():
    print_students_pythonic()
    print_students_len()
    

def print_students_pythonic():
    for student in students:
        print(student)


def print_students_len():
    for i in range(len(students)):
        print(i+1, students[i])


main()