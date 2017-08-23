#! python3
# Regex Search - Open a file then look for a specific phrase.

import re


# user input
print("We're going to search for a string in a file \n")
searchString = input("Write the string you want to search for: \n")

# open and read file
file = open('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff\\sample.txt',
            encoding='utf8')
content = file.read()
file.close()

# create regex
regex = re.compile(r".*%s.*" % searchString)

# print out the lines with match
if regex.findall(content) is None:
    print("No matches was found.")
else:
    print(regex.findall(content))
    
