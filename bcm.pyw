#! python3
# mcb.pyw - create a multiclipboard tool
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - loads all keywords to clipboard.


import shelve, pyperclip, sys

#open the shelve
mcbShelf = shelve.open('bcm')

#save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#either copy keys to clipboard or copy value of a key
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
       pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
       pyperclip.copy(mcbShelf[sys.argv[1]])

#close out the shelve
mcbShelf.close()
