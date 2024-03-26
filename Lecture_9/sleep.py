def main():
    n = int(input("What's n? "))
    
    # for i in range(n):
    #     print(sheep(i))

    # print(*sheep_flock(n), sep='\n')

    print(*sheep_generator(n), sep='\n')


def sheep(n):
    return "🐑 " * n


def sheep_flock(n):
    flock = []
    for i in range(n):
        flock.append("🐑 " * i)
    return flock


def sheep_generator(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
