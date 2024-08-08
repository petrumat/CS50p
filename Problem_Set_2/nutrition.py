# Define dictionary for fruit and calories
fruit_calories_dict = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

def main():
    # Get item from user (case-insensitively)
    item = input("Item: ")
    item = item.lower()

    # Show nutritional facts, if any
    nutritional_facts(item)


def nutritional_facts(item):
    # Find item in fruit_calories dictionary
    if item in fruit_calories_dict:
        # Show corresponding calories
        print(f"Calories: {fruit_calories_dict[item]}")


if __name__ == "__main__":
    main()
