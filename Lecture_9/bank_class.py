class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, n):
        self.balance += n

    def withdrow(self, n):
        self.balance -= n

    def __str__(self):
        return f"{self.balance}"


def main():
    account = Account()
    print("Balance:", account)
    
    account.deposit(100)
    print("Balance:", account)
    
    account.withdrow(50)
    print("Balance:", account)


if __name__ == "__main__":
    main()