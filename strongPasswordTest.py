import re

def isStrongPassword(text):

    upperRegex = re.compile(r'[A-Z]+')    
    lowerRegex = re.compile(r'.*[a-z]+')
    digitRegex = re.compile(r'\d+')


    if len(text) < 8:
        print('You need at least eight characters')
    elif upperRegex.search(text) == None:
        print('You need an UPPER case character.')
    elif lowerRegex.search(text) == None:
        print('You need to include a lower case character.')
    elif digitRegex.search(text) == None:
        print('You need to include a digit')
    else:
        print('STRONG PASSWORD')

text = 'paUwordtrre'

isStrongPassword(text)

   
