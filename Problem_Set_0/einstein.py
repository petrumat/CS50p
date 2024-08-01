def main():
    # Get mass from user
    mass = int(input("m: "))

    light_speed = 300000000

    # Calculate energy
    energy = mass * light_speed * light_speed

    # Print energy
    print(energy)


if __name__ == "__main__":
    main()
