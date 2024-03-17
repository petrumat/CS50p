def main():
    hello()
    goodbye()


def hello(name = "world"):
    print(f"hello, {name}")


def goodbye(name = "world"):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()