import pandas as pd
from fpdf import FPDF as fd
import glob
from pathlib import Path

filepaths = glob.glob("textfiles/*txt")
pdf = fd(orientation="P", unit="mm", format="A4")

for filepath in filepaths:

    with open(filepath, "r") as file:
        content = file.read()

    filename = Path(filepath).stem
    name = filename.title()
    
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size =16)
    pdf.cell(w=50, h=10, txt=name)
    pdf.line(10,20,200,20)
    pdf.set_font(family="Times", size =10)
    pdf.ln(10)

    pdf.multi_cell(0, 6, txt=content)



pdf.output("output.pdf")

