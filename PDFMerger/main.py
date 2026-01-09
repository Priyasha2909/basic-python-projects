from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs =[]

n = int(input("How many PDFs do you want to merge?\n"))

for i in range(0,n):
    pdfName = input(f"Enter name of {i+1} PDF: ")
    pdfs.append(pdfName)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged_pdf.pdf")
merger.close()        