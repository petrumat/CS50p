import csv

def main():
    save_students_writer()
    save_students_DictWriter()

    
def save_students_writer():
    name = input("What's your name? ")
    home = input("What's your home? ")
    
    with open("students_archive.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])


def save_students_DictWriter():
    name = input("What's your name? ")
    home = input("What's your home? ")
    
    with open("students_archive.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow(["name": name, "home": home])
    

if __name__ == "__main__":
    main()