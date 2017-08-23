#! python3
# Create a mew MadlIb with user inputs. Currently faisl with punctuation.

import re

madLibFile = open('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff\\madLibProject.txt')

with open('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff\\madLibProject.txt') as madLibFile:
     madLib = madLibFile.read()

nounRegex = re.compile(r'NOUN\.?\,?', re.I)
adjRegex = re.compile(r'ADJECTIVE\.?\,?', re.I)
verbRegex = re.compile(r'VERB\.?\,?', re.I)

# REGEX w/ . or , working
y = 0
newMadLib = []

for i in range(1):
    newMadLibFile = open('MadLib%s.txt' % (i + 1), 'w')

for word in madLib.split():

    newMadLib.append(word)
    if nounRegex.search(word) != None:
        x = input('Enter a NOUN: ')
        newMadLib[y] = x
            
    elif adjRegex.search(word) != None:
        x = input('Enter a ADJECTIVE: ')
        newMadLib[y] = x

    elif verbRegex.search(word) != None:
        x = input('Enter a VERB: ')
        newMadLib[y] = x
    y+=1

newMadLib = (' ').join(newMadLib)

newMadLibFile.write(newMadLib)

newMadLibFile.close()

print(madLib)
print (newMadLib)
