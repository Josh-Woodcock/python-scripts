#! python3
# selectiveCopy.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import os
import shutil

def selectiveCopy(folder):
    folder = os.path.abspath(folder)
    
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith('.txt'):
                continue
            # shutil.copy(filename, C:\\Path\\To\\Directory) #Commented out to protect against accidental copying
            print('Copying ' + filename + '...') #Print only to verify working correctly

selectiveCopy(r'C:\\delicious')
print('Done')

