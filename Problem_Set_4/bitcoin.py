from sys import argv, exit
import requests


def main():
    # Get amount of bitcoins from command-line argument
    bitcoins = get_bitcoins()

    # Get bitcoin current price
    bpi_price = request_bitcoin_price_index()

    # Calculate required price
    total = bitcoins * bpi_price

    # Show total price formatted
    print(f"${total:,.4f}")


def get_bitcoins():
    # Verify if command-line argument exists
    if len(argv) != 2:
        exit("Missing command-line argument")
    else:
        try:
            # Convert command-line argument to float
            total_bitcoins = float(argv[1])

            # Discard negative numbers
            if total_bitcoins < 0:
                exit("Command-line argument is not a positive number")
            else:
                return total_bitcoins

        except ValueError:
            # Terminate execution if command-line argument isn't a number
            exit("Command-line argument is not a number")


def request_bitcoin_price_index():
    try:
        # Request currentprice.json
        req = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        # Get bitcoin USD rate_float
        return req.json()['bpi']['USD']['rate_float']

    except requests.RequestException:
        # Terminate execution if request raised error
        exit("CoinDesk Bitcoin Price Index request failed")


if __name__ == "__main__":
    main()
