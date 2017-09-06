#! python3
# deleteUneeded.py - finds files in given directory that are larger than 100MB.
# Prints filename w/ absolute path.

import os
import shutil
from hurry.filesize import size, alternative 

def delUneeded(folder):

    folder = os.path.abspath(folder)
    
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(foldername + '/' + filename)
            if fileSize < 30000000:
                continue

            bigSize = size(fileSize, system=alternative)
            
            print(filename + ' - ' + str(bigSize))
            #os.unlink(filename) #Commented out to protect against accidental deletion
            print('Deleting ' + filename + '...')
            
delUneeded('C:\\Users\\Josh\\Downloads')
print('Done')
