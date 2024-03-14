def main():
    x = float(input("What's x? "))
    print(f"x squared is {square(x):,.10g}") # Formats result to max 10 decimals,
                                # but no unnecessary 0 to 10 decimals.


def square(a = 0.0):
    return a * a
    # or a ** 2
    # oe pow(a, 2)


main()