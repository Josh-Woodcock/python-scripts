import PyPDF2

# Open file you want to encrypt and read it
pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
3
# for each page copy to pdfFileWriter object
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# encrypt this object with password
pdfWriter.encrypt('swordfish')

# create an ecncrypted PDF suing this object
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)

# close the resulting file
resultPdf.close()
