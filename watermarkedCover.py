import PyPDF2

# Open and Read PDF you want to watermark
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)

# Get first page
minutesFirstPage = pdfReader.getPage(0)

# open the watermark
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

# Merge the first page with the wayermark
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

# write page object and add watermarked page to the end
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

# for each page in the PDF add it to PdfFile object
for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# create final PDF
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

# close files
minutesFile.close()
resultPdfFile.close()