import PyPDF2

# open and read PDF file
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

# get Page and rotate
page = pdfReader.getPage(0)
page.rotateClockwise(90)

# Write the Page
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)

# Create new PDF
resultPdfFile = open('rotatedPage.pdf', 'wb')

# write the rotated PDF page
pdfWriter.write(resultPdfFile)

# close all files
resultPdfFile.close()
minutesFile.close()
