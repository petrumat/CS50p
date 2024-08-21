# Import necessary modules
from sys import argv, exit
from os import mkdir
from io import open


# main() expects one command-line argument (directory/program name)
def main():
    if len(argv) != 2:
        # Exit if directory/program name is missing
        exit(f"Expected directory/program name")

    try:
        # Create directory in root
        mkdir(argv[1])
    except FileExistsError:
        # Exit if directory already exists
        exit(f"Directory '{argv[1]}/' already exists")

    # Determine python program's name and path
    prog_name = argv[1] + '.py'
    prog_path = argv[1] + '/' + prog_name

    # Create python program (with main() function template)
    with open(prog_path, 'a') as prog:
        template = main_function_template()
        prog.write(template)


# Create main() function template as str
def main_function_template():
    template = '\
def main():\n\
    pass\n\
\n\
\n\
if __name__ == "__main__":\n\
    main()'
    
    return template


if __name__ == "__main__":
    main()
