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

    pdf.ln(10)

    pdf.set_font(family="Times", size=10 , style="B")
    columns = list(df.columns)
    columns = [item.replace("_"," ").title() for item in columns]



    pdf.cell(w=30, h=8, txt=columns[0], border=True)
    pdf.cell(w=50, h=8, txt=columns[1],  border=True)
    pdf.cell(w=40, h=8, txt=columns[2],  border=True)
    pdf.cell(w=30, h=8, txt=columns[3],  border=True)
    pdf.cell(w=40, h=8, txt=columns[4],  border=True)



    """
    pdf.cell(w=30, h=8, txt="Product id", border=True)
    pdf.cell(w=50, h=8, txt="Product name",  border=True)
    pdf.cell(w=40, h=8, txt="Amount purchased",  border=True)
    pdf.cell(w=30, h=8, txt="Price per unit",  border=True)
    pdf.cell(w=40, h=8, txt="Total price",  border=True)
    """

    pdf.ln(8)
    total_amount=0

    for index, row in df.iterrows():
       total_amount = total_amount + row["total_price"]
       pdf.set_font(family="Times", size=10)
       pdf.set_text_color(80,80,80)
       pdf.cell(w=30, h=8, txt=f"{row["product_id"]}", border=True)
       pdf.cell(w=50, h=8, txt=f"{row["product_name"]}",  border=True)
       pdf.cell(w=40, h=8, txt=f"{row["amount_purchased"]}",  border=True)
       pdf.cell(w=30, h=8, txt=f"{row["price_per_unit"]}",  border=True)
       pdf.cell(w=40, h=8, txt=f"{row["total_price"]}",  border=True)
       pdf.ln(8)

    pdf.ln(20)
    pdf.set_font(family="Times", size=12, style="B")
    
    pdf.cell(w=30, h=8, txt="Total amount", border=True)
    pdf.cell(w=30, h=8, txt=f"{total_amount}",  border=True)



   

    



    pdf.output(f"PDFs/{filename}.pdf")
    


