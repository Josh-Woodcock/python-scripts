#! python3
# addPrefiz.py - adds prefix of your choice to files in chosen directory

import shutil, os, re

# create regex

prefixRegex = re.compile(r'^spam_')

for oldFileName in os.listdir('.'):

    mo = prefixRegex.search(oldFileName)

    if mo != None:
        continue

    newFileName = 'spam_%s' % oldFileName

    absWorkingDir = os.path.abspath('.')
    oldFilePath = os.path.join(absWorkingDir, oldFileName)
    newFilePath = os.path.join(absWorkingDir, newFileName)

    print('Renaming "%s" to "%s"...' % (oldFileName, newFileName))
    shutil.move(oldFilePath, newFilePath)
