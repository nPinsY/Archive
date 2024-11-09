from fpdf import FPDF
import re

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)

class Shirt:
    pattern = r"[a-z ]+"
    all = []

    def __init__(self, name: str):
        # Validate
        if not re.fullmatch(Shirt.pattern, name, re.IGNORECASE):
            raise ValueError("Invalid name format")
        # Assign
        self.name = name
        # Append
        Shirt.all.append(self)

    def create(self):
        pdf = PDF()
        pdf.add_page(orientation="portrait", format="a4")
        pdf.set_font("helvetica", size=24)
        pdf.set_text_color(255,255,255)
        pdf.cell(0, 213, f"{self.name} took CS50", align="C")
        pdf.output("shirtificate.pdf")

def main():
    name1 = Shirt(input("Name: "))
    name1.create()

if __name__ == "__main__":
    main()