def main():
    # name = input("What's the name? ")
    # house = input("What's the house? ")
    
    # name = get_name()
    # house = get_house()
    
    # student = get_student_tuple()
    # print(f"{student[0]} is in house {student[1]}")
    
    # student = get_student_list()
    # print(f"{student[0]} is in house {student[1]}")
    
    student = get_student_dict()
    if student['name'] == "Padma":
        student['house'] = "Ravenclaw"
    print(f"{student['name']} is in house {student['house']}")


def get_name():
    return input("What's the name? ")

def get_house():
    return input("What's the house? ")

def get_student_tuple():
    name = input("What's the name? ")
    house = input("What's the house? ")
    return (name, house)    # this returns a tuple (immutable list)

def get_student_list():
    name = input("What's the name? ")
    house = input("What's the house? ")
    return [name, house]    # this returns a list

def get_student_dict():
    name = input("What's the name? ")
    house = input("What's the house? ")
    return {"name": name, "house": house}    # this returns a dictionary

if __name__ == "__main__":
    main()