from fpdf import FPDF, Align

def main():
    name = input("Name: ")
    make_shirt(name)


def make_shirt(name):
    # Create FPDF instance with Portrait orientation and A4 format
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    # Add new page
    pdf.add_page()

    # Set y lower than current for shirtificate "title"
    pdf.set_y(pdf.get_y()+20)

    # Set any font you want in your size
    pdf.set_font('helvetica', size=50)

    # Add text centered horizontally (and in cell)
    pdf.cell(text="CS50 Shirtificate", align="C", center=True)

    # Add shirt image centered horizontally, lowered than pdf "title" and
    # scale horizontally to the full page width
    pdf.image("shirtificate.png", x=Align.C, y=pdf.get_y()+40, w=pdf.epw)

    # Set y lower than current for shirtificate "title"
    pdf.set_y(pdf.get_y()+100)

    # Make size smaller for shirt text
    pdf.set_font_size(size=24)

    # Set color to white for shirt text
    pdf.set_text_color(255, 255, 255)

    # Add shirt text in center
    pdf.cell(text=f"{name} took CS50", align="C", center=True)

    # Save pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
