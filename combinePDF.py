import PyPDF2

# Choose two PDFs to combine

pdf1 = input('Enter a filename: ')
pdf2 = input('Enter a filename: ')

# Opens the two files to combine
pdf1File = open('pdf1.pdf', 'rb')
pdf2File = open('pdf2.pdf', 'rb')

# Reads the contents of the two files
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# PDF object for combined file
pdfWriter = PyPDF2.PdfFileWriter()

# For each page in PDF1 add it to pdfWriter object
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# For each page in PDF2 add it to pdfWriter object
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Create new output PDF

pdfOutputName = input('Enter a filename for new combined file: ')
pdfOutputFile = open('pdfOutputName.pdf', 'wb')

# Write the content to new file
pdfWriter.write(pdfOutputFile)

# Close all files
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
