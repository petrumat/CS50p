class Jar:
    def __init__(self, capacity=12):
        # Assign capacity to function argument
        self.capacity = capacity

        # Start with 0 cookies by default
        self.size = 0


    def __str__(self):
        return '🍪' * self.size


    # increase number of cookies from jar
    def deposit(self, n):
        if type(n) == int:
            if n < 0:
                # n can't be a negative number
                raise ValueError("Wrong number")
        else:
            # n must be a number
            raise TypeError("Expected number")

        if self.size + n > self.capacity:
            # Should not exceed jar capacity
            raise ValueError("Too many cookies")

        # Update size depositing cookies
        self.size += n

    # reduce number of cookies from jar
    def withdraw(self, n):
        if type(n) == int:
            if n < 0:
                # n can't be a negative number
                raise ValueError("Wrong number")
        else:
            # n must be a number
            raise TypeError("Expected number")

        if self.size - n < 0:
            # Should not withdraw more than size cookies
            raise ValueError("Too few cookies")

        # Update size withdrawing cookies
        self.size -= n


    # capacity getter
    @property
    def capacity(self):
        return self._capacity

    # capacity setter
    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            # Capacity can't be 'None'
            raise ValueError("Missing capacity")

        if type(capacity) == int:
            if capacity < 0:
                # Capacity can't be a negative number
                raise ValueError("Negative capacity")
        else:
            # Capacity should be 'int'
            raise TypeError("Wrong capacity type")

        # Update capacity
        self._capacity = capacity


def main():
    jar = get_jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(2)
    print(jar)


def get_jar():
    capacity = input("What's the jar capacity? ")
    if not capacity.isnumeric():
        raise ValueError("Expected a number")

    return Jar(int(capacity))


if __name__ == "__main__":
    main()
