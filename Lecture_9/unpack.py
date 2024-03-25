


def main():
    # unpack_name()
    
    # # Calling function with hardcoded values
    # print(total(100, 50, 25), "Knuts")
    
    # # Calling function with every item in list
    # coins_list = [100, 50, 25]
    # print(total(coins_list[0], coins_list[1], coins_list[2]), "Knuts")
    
    # # Calling function with a packed list and letting python unpack it
    # print(total(*coins_list), "Knuts")
    
    # # Calling function with named parameters
    # print(total(galleons=100, sickles=50, knuts=25), "Knuts")
    
    # # Calling function with a dictionary
    # coins_dict = {"sickles": 50, "knuts": 25, "galleons": 100}
    # print(total(coins_dict["galleons"], coins_dict["sickles"], coins_dict["knuts"]), "Knuts")
    
    # # Calling function with a packed dictionary and letting python unpack it
    # print(total(**coins_dict), "Knuts")    

    f_args(100, 50, 25)
    f_args(100, 50, 25, 5)
    f_kwargs(galleons=100, sickles=50, knuts=25)
    f_kwargs(galleons=100, sickles=50, knuts=25, pennies=5)


def unpack_name():
    first, _ = input("What's your name? ").split(" ")
    print(f"Hello, {first}")


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def f_args(*args, **kwargs):
    print("Positional:", args)

def f_kwargs(*args, **kwargs):
    print("Named:", kwargs)


if __name__ == "__main__":
    main()