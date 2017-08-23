#! python3
# censorCreditCard.py - Finds credit card numbers and censors all digits but final 4 

import pyperclip, re

text = str(pyperclip.paste())

ccRegex = re.compile(r'\d{14,17}')              

matches = []

for cc in ccRegex.findall(text):
    matches.append(cc)

stringMatches = '\n'.join(matches)

censoredRegex = ccRegex.sub(r'***** ******', stringMatches)



print(censoredRegex)






