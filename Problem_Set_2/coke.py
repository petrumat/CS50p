def main():
    coke_machine()


def coke_machine():
    # Set the remaining amount
    remaining = 50

    # Define the possible coin types
    possible_coins = [25, 10, 5]

    while remaining > 0:
        # Start with the remaining amount
        print(f"Amount Due: {remaining}")

        # Get coin from user
        user_coin = int(input("Insert Coin: "))
        # Reject unwanted coins
        if user_coin not in possible_coins:
            continue

        # Update the remaining amount
        remaining -= user_coin
        # If amount is finished, show owned change as positive amount
        if remaining <= 0:
            print(f"Change Owed: {remaining * (-1)}")


if __name__ == "__main__":
    main()
