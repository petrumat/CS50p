students_dict = {}
students_list = []

def main():
    # get_students_dict()
    # get_students_dict_pythonic()
    # print_students_dict()
    # get_students_list()
    get_students_list_pythonic()
    # print_students_list()
    # print_sorted_students_list()
    # print_reverse_sorted_students_list()
    # print_sorted_students_list_pythonic()
    # print_reverse_sorted_students_list_pythonic()
    # print_sorted_students_list_by_house()
    # print_reverse_sorted_students_list_by_house()
    print_sorted_students_list_by_house_pythonic()
    print_reverse_sorted_students_list_by_house_pythonic()
    
    
def get_students_dict():
    with open("students.csv") as file:
        for line in file:
            student_details = line.rstrip().split(',')
            students_dict.update({student_details[0] : student_details[1]})


def get_students_dict_pythonic():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(',')
            students_dict.update({name : house})
            

def print_students_dict():
    print("Students' dictionary:")
    for student in students_dict:
        print(student, "is in", students_dict[student])


def get_students_list():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(',')
            student = {}
            student["name"] = name
            student["house"] = house
            students_list.append(student)


def get_students_list_pythonic():
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(',')
            students_list.append({"name": name, "house": house})


def print_students_list():
    print("Students' list:")
    for student in students_list:
        print(f"{student['name']} is in {student['house']}")


def get_name(student):
    return student["name"]
    
def print_sorted_students_list():
    print("Sorted students' list:")
    for student in sorted(students_list, key=get_name):
        print(f"{student['name']} is in {student['house']}")


def print_reverse_sorted_students_list():
    print("Reverse sorted students' list:")
    for student in sorted(students_list, key=get_name, reverse=True):
        print(f"{student['name']} is in {student['house']}")


def print_sorted_students_list_pythonic():
    print("Sorted students' list:")
    for student in sorted(students_list, key=lambda student: student["name"]):
        print(f"{student['name']} is in {student['house']}")


def print_reverse_sorted_students_list_pythonic():
    print("Reverse sorted students' list:")
    for student in sorted(students_list, key=lambda student: student["name"], reverse=True):
        print(f"{student['name']} is in {student['house']}")


def get_house(student):
    return student["house"]
    
def print_sorted_students_list_by_house():
    print("Sorted students' list by house:")
    for student in sorted(students_list, key=get_house):
        print(f"{student['name']} is in {student['house']}")


def print_reverse_sorted_students_list_by_house():
    print("Reverse sorted students' list by house:")
    for student in sorted(students_list, key=get_house, reverse=True):
        print(f"{student['name']} is in {student['house']}")


def print_sorted_students_list_by_house_pythonic():
    print("Sorted students' list by house:")
    for student in sorted(students_list, key=lambda student: student["house"]):
        print(f"{student['name']} is in {student['house']}")


def print_reverse_sorted_students_list_by_house_pythonic():
    print("Reverse sorted students' list by house:")
    for student in sorted(students_list, key=lambda student: student["house"], reverse=True):
        print(f"{student['name']} is in {student['house']}")


if __name__ == "__main__":
    main()