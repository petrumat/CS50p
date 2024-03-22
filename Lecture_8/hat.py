import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        return(f"{name} is in house {house}")


def main():
    print(Hat.sort("Harry"))


if __name__ == "__main__":
    main()