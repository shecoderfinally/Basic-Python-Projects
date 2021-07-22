from PyPDF2 import PdfFileWriter, PdfFileReader

pdfwriter = PdfFileWriter()
pdf = PdfFileReader("OpenUp.pdf")

for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
passw = "HelloMia"
pdfwriter.encrypt(passw)

with open('new.pdf', 'wb') as f:
    pdfwriter.write(f)
    f.close()
