#! python3
# pdfParanoia.py will look for all pDF files in a directory and encrypt them
# with password given by user

import os, PyPDF2, send2trash

# Prompt user for password
password = input('Enter a password to encrypt PDFs with: ')

os.chdir('C:\\delicious')

# Look for PDFs in file directories
for foldername, subfolders, filenames in os.walk('.'):
    for filename in filenames:
            if filename.endswith('.pdf'):
                # Read PDF
                print(filename)
                pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
                # Create write object
                pdfWriter = PyPDF2.PdfFileWriter()
                # Get all pages in PDF and add to write object
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))

                # Encrypt the write object with user provided password, and write said object to new file

                print('Encrypting ' + filename)
                pdfWriter.encrypt(password)

                pdfOutputFile = open('encrypted-' + filename, 'wb')
                pdfWriter.write(pdfOutputFile)
                pdfOutputFile.close()

                # # Test that PDF is encryped. If it is send it to trash
                # pdfReader2 = PyPDF2.PdfFileReader(open(filename + '_encrypted', 'rb'))
                # if pdfReader2.isEncrypted is True:
                #     send2trash.send2trash(filename)


