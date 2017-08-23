#! python3
# zeroStripper.py - strips zero's from filenames

import shutil, os, re

zeroRegex = re.compile(r'0+')

for oldFileName in os.listdir('.'):


    if zeroRegex is None:
        continue
    else:
        newFileName = zeroRegex.sub('',(oldFileName))

    absWorkingDir = os.path.abspath('.')
    oldFilePath = os.path.join(absWorkingDir, oldFileName)
    newFilePath = os.path.join(absWorkingDir, newFileName)

    print('Renaming "%s" to "%s"...' % (oldFileName, newFileName))
    shutil.move(oldFilePath, newFilePath)
