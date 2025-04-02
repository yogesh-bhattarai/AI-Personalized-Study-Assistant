import re
from pdfminer.high_level import extract_text
import pdf2image
import pytesseract

def get_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_ocr(pdf_path):
    images= pdf2image.convert_from_path(pdf_path)
    text= "\n".join([pytesseract.image_to_string(img)for img in images])
    return text
h1=extract_text_ocr(r"C:\Users\yogass\Desktop\Study_Assistance\sample syallubus.pdf")
print(h1)

result= get_text_from_pdf(r"C:\Users\yogass\Desktop\MYCV.pdf")
#print(result)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text
hey= clean_text(result)
print(hey)