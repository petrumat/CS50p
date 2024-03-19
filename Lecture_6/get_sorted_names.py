names = []

def main():
    get_list()
    print_sorted_list()
    print_reverse_sorted_list()
    print_sorted_file()
    print_reverse_sorted_file()


def get_list():
    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())
            
    
def print_sorted_list():
    print("Sorted names from list:")
    for name in sorted(names):
        print(name)
    
    
def print_reverse_sorted_list():
    print("Reverse sorted names from list:")
    for name in sorted(names, reverse=True):
        print(name)
        
        
def print_sorted_file():
    print("Sorted names from file:")
    with open("names.txt") as file:
        for line in sorted(file):
            print(line.rstrip())
            
            
def print_reverse_sorted_file():
    print("Reverse sorted names from file:")
    with open("names.txt") as file:
        for line in sorted(file, reverse=True):
            print(line.rstrip())
            
            
if __name__ == "__main__":
    main()