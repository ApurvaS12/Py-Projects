import pandas as pd
from fpdf import FPDF as fd
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]


    pdf = fd(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=70, h=8, txt=f"Invoice number: {invoice_nr}")

    date = filename.split("-")[1]
    pdf.ln(10)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")

   

    



    pdf.output(f"PDFs/{filename}.pdf")
    


