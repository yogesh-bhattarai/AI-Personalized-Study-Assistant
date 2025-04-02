import re
from pdfminer.high_level import extract_text

def get_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


result= get_text_from_pdf(r"C:\Users\yogass\Desktop\MYCV.pdf")
#print(result)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return text
hey= clean_text(result)
print(hey)