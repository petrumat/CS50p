def main():
    x = float(input("What's x? "))
    print(f"x squared is {square(x):,.10g}") # Formats result to max 10 decimals,
                                # but no unnecessary 0 to 10 decimals.


def square(a = 0.0):
    a **= 2
    return a
    # or return a * a
    # or return a ** 2
    # oe return pow(a, 2)


main()