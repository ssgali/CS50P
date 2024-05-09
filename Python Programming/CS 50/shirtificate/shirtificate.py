from pathlib import ntpath
import sys
from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 25)
    pdf.cell(0,0,"CS50 Shirtificate",align = "C",markdown = True)
    pdf.ln(100)
    pdf.image("shirtificate.png", x="C",y=40)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,0,f"{name} took CS50",align = "C")
    pdf.output("shirtificate.pdf")
if __name__ == "__main__":
    main()