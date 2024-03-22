# class Student:  # by convention classes names are capitalized
#     ...  # to skip the implementation of a class use "..."

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    # similar to toString from Java
    def __str__(self):
        return f"{self.name} is from house {self.house}"

    @classmethod
    def get(cls):
        name = input("What's the name? ")
        house = input("What's the house? ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()