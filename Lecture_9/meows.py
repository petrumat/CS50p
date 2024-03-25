MEOWS = 3

class Cat:
    CLASS_MEOWS = 3
    
    def meow(self):
        print("Meows from Cat object:")
        for _ in range(Cat.CLASS_MEOWS):
            print("meow")


def main():
    # print("Meows from main:")
    # for _ in range(MEOWS):
    #     print("meow")
    
    cat = Cat()
    cat.meow()


if __name__ == "__main__":
    main()