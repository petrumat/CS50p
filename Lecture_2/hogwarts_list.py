# Defines a global list accessible in every function (after it)
students = ["Hermione", "Harry", "Ron", "Draco"]


def main():
    print_students()
    print_students_pythonic()
    print_students_len()
    

def print_students():
    # Demonstrates indexing into a list
    print(students[0])
    print(students[1])
    print(students[2])
    print(students[3])
    

def print_students_pythonic():
    # Demonstrates iterating over a list
    for student in students:
        print(student)


def print_students_len():
    # Demonstrates iterating over and indexing into a list
    for i in range(len(students)):
        print(i+1, students[i])


main()