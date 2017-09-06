#! python3
# backupPyZip.py - Copies an entire folder and its .py and .txt contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupPyZip(folder):
    # Backup the netire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP File

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    #TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Addl all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            elif filename.endswith('.py') or filename.endswith('.txt'):
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')



backupPyZip('C:\\Users\\Josh\\Anaconda3\\automate-the-boring-stuff')
