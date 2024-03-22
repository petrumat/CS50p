# class Student:  # by convention classes names are capitalized
#     ...  # to skip the implementation of a class use "..."

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    # similar to toString from Java
    def __str__(self):
        return f"{self.name} is from house {self.house}"

    # similar to getter from Java
    @property
    def name(self):
        return self._name

    # similar to setter from Java
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # similar to getter from Java
    @property
    def house(self):
        return self._house

    # similar to setter from Java
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("What's the name? ")
    house = input("What's the house? ")
    return Student(name, house) # create class Student object from initializer call with parameters


if __name__ == "__main__":
    main()