#! python3
# bruteForce.py - searches dictionary.txt for password to encrypted PDF file

import PyPDF2

# Get dictionary file
dictFile = open('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff\\dictionary.txt')

# Open dictionary file
with open('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff\\dictionary.txt') as dictFile:
    dictionary = dictFile.read()

# Create list of passwords
passwordList = []

# For each word in dictionary add lower and UPPER case versions to password list
for word in dictionary.split():

    lowerCase = word.lower()
    passwordList.append(lowerCase)

    upperCase = word.upper()
    passwordList.append(upperCase)

print(passwordList)

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))

# Run all passwords in list through decryption
for password in passwordList:
    if pdfReader.decrypt(password) == 1:
        solved = password
        break
    else:
        continue
print('The password is ' + solved)

