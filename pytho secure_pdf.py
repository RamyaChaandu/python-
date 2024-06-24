from PyPDF2 import PdfReader, PdfWriter
def add_password(input_pdf, output_pdf, password):
    # Create a PdfReader object
    reader = PdfReader(input_pdf)
    # Create a PdfWriter object
    writer = PdfWriter()
    # Copy all pages from the reader to the writer
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])
    # Encrypt the PDF with the given password
    writer.encrypt(password)
    # Write the encrypted PDF to a new file
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)
# Example usage
input_pdf_path = "C:/Users/LENOVO/OneDrive/Documents/one.pdf"
output_pdf_path = 'C:/Users/LENOVO/OneDrive/Documents/out.pdf'
password = '3056'

add_password(input_pdf_path, output_pdf_path,password)