#! python3
# censorCreditCard.py - Finds credit card numbers and censors all digits but final 4 

import pyperclip, re

visaCCRegex = re.compile(r'4\d{15}')
mastercardCCRegex = re.compile(r'5\d{15}')
discoverCCRegex = re.compile(r'6\d{15}')
aeCCRegex = re.compile(r'3\d{14}')

ccRegex = re.compile(r'''(
    4\d{15}|            # Visa
    5\d{15}|            # Mastercard
    6\d{15}|            # Discover
    3\d{14}             # American Express
    ) ''', re.VERBOSE)
    

text = str(pyperclip.paste())

matches = []

for cc in ccRegex.findall(text):
    matches.append(cc)

# Copy Results to the clipboard.

print(matches)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    for match in matches:
        if visaCCRegex:
            print('Visa Cards')
            print('\n'.join(matches))

    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Visa credit card details found')



