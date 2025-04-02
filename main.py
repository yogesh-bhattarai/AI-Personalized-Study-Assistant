import re
from pdfminer.high_level import extract_text

def get_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


result= get_text_from_pdf(r"C:\Users\yogass\Desktop\MYCV.pdf")

print(result)