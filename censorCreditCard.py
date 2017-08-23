#! python3
# censorCreditCard.py - Finds credit card numbers and censors all digits but final 4 

import pyperclip, re

text = str(pyperclip.paste())

ccRegex = re.compile(r'\d{15,16}')              

matches = []

for cc in ccRegex.findall(text):
    matches.append(cc)

# Results

if len(matches) > 0:

    stringMatches = ' '.join(matches)

    print(stringMatches)

    censoredMatches = []

    for cc in stringMatches:
        matches.append(ccRegex.sub(r'*', stringMatches))
    
    print(censoredMatches)
    


   
else:
    print('No credit card details found')



