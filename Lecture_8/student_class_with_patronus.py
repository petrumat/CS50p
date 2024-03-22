# class Student:  # by convention classes names are capitalized
#     ...  # to skip the implementation of a class use "..."

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} is from house {self.house} with patronus {self.patronus}"
    
    def charm(self):
        return "charm ha ha"
        # match self.patronus:
        #     case "Stag" :
        #         return "🐴"
        #     case "Otter":
        #         return "🦦"
        #     case "Jack Russel terrier":
        #         return "🐶"
        #     case _:
        #         return "🪄"


def main():
    # student = get_student()
    student = get_student_initializer()
    print(student.charm())


def get_student():
    student = Student() # create class Student object
    student.name = input("What's the name? ")   # assign name attribute
    student.house = input("What's the house? ")   # assign house attribute
    return student


def get_student_initializer():
    name = input("What's the name? ")
    house = input("What's the house? ")
    patronus = input("What's the patronus? ")
    return Student(name, house, patronus) # create class Student object from initializer call with parameters


if __name__ == "__main__":
    main()