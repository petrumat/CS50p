students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry",    "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron",      "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco",    "house": "Slytherin",  "patronus": None},
]


def main():
    # print("Hermione is in house " + students["Hermione"])
    print_students()
    
    
def print_students():
    for student in students:
        print(student["name"], student["house"], student["patronus"], sep=', ')


main()