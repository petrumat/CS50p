students = [
    {"name": "Hermione", "house": "Gryffindor", "element": "fire", "matter": "plasma"},
    {"name": "Harry", "house": "Gryffindor", "element": "fire", "matter": "plasma"},
    {"name": "Ron", "house": "Gryffindor", "element": "fire", "matter": "plasma"},
    {"name": "Draco", "house": "Slytherin", "element": "water", "matter": "liquid"},
    {"name": "Padma", "house": "Ravenclaw", "element": "air", "matter": "gas"},
    {"name": "Cedric", "house": "Hufflepuff", "element": "earth", "matter": "solid"},
]


def main():
    # print(*sorted_students_from_house("Gryffindor"), sep='\n')

    # print(is_from_house(students[0], "Gryffindor"))

    """
    Print whole result, which is a list of dictionaries, and then names
    """
    print(*(results := filter_by_house()), sep="\n")
    for result in results:
        print(result["name"])


def sorted_students_from_house(house):
    global students

    gryffindors = [student["name"] for student in students if student["house"] == house]

    return sorted(gryffindors)


def filter_by_house():
    global students

    """
    Using filter can be done by defining a true/false function or by
    using a no name lambda function
    """
    # gryffindors = filter(is_from_house, students)
    gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)

    """
    Returns list of dictionaries (similar to students variable),
    either as is or sorted by "name".
    """
    # return gryffindors
    return sorted(gryffindors, key=lambda gryffindor: gryffindor["name"])


def is_from_house(student):
    """
    Either return conditional will work. Bought pythonic.
    """
    # return True if student["house"] == house else False
    return student["house"] == "Gryffindor"


if __name__ == "__main__":
    main()
