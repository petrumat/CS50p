def main():
    students = [
        {"name": "Hermione", "house": "Gryffindor"},
        {"name": "Harry",    "house": "Gryffindor"},
        {"name": "Ron",      "house": "Gryffindor"},
        {"name": "Draco",    "house": "Slytherin"},
        {"name": "Padma",    "house": "Ravenclaw"},
    ]
    
    # print_houses_list(students)
    print_houses_set(students)


def print_houses_list(students):
    houses = []
    # houses = list() # create a list by calling constructor
    
    for student in students:
        if student["house"] not in houses:
            houses.append(student["house"])
    
    print("Houses from a sorted list:")
    for house in sorted(houses):
        print(house)


def print_houses_set(students):
    houses = set()
    
    for student in students:
        houses.add(student["house"])
    
    print("Houses from a sorted set:")
    for house in sorted(houses):
        print(house)


if __name__ == "__main__":
    main()