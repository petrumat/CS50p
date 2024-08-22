# Import necessary modules
from sys import argv, exit
from PIL import Image, ImageOps


# main() expects two command-line argument (input_file output_file)
def main():
    # Exit if program call is incorrect
    if len(argv) < 3:
        exit(f"Too few command-line arguments")
    elif len(argv) > 3:
        exit(f"Too many command-line arguments")

    # Exit if files' name don't end in '.jpg', '.jpeg' or '.png'
    if not argv[1].endswith('.jpg') \
    and not argv[1].endswith('.jpeg') \
    and not argv[1].endswith('.png'):
        exit(f"Invalid input")

    # Exit if files' name don't end in same extension
    if (argv[1].endswith('.jpg') and not argv[2].endswith('.jpg')) \
    or (argv[1].endswith('.jpeg') and not argv[2].endswith('.jpeg'))\
    or (argv[1].endswith('.png') and not argv[2].endswith('.png')):
        exit(f"Input and output have different extensions")

    # Overlay P-Shirt
    overlay_p_shirt(argv[1], argv[2])


def overlay_p_shirt(input_file, output_file):
    # Try opening shirt.png file
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        exit("shirt.png file not found")

    # Determine shirt dimensions
    size = shirt.size

    # Try opening input file
    try:
        input_image = Image.open(input_file)
    except FileNotFoundError:
        exit("Input file not found")

    # Fit input image to shirt size
    input_image = ImageOps.fit(input_image, size)

    # Paste shirt image onto input_file
    input_image.paste(shirt, shirt)

    # Save the final image
    input_image.save(output_file)


if __name__ == "__main__":
    main()
