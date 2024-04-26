from fpdf import FPDF as fd
import pandas as pd

pdf = fd(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)

df = pd.read_csv("topics.csv")


for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt= row["Topic"], align="L", ln=1 )
    pdf.line(10,21,200,21)
    pages = int(row["Pages"])

    while pages>1:
        pdf.add_page()
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=20,txt=row["Topic"], align="R")

        pages = pages-1
    


pdf.output("output.pdf")
