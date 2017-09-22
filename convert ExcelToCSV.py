import os
import openpyxl
import csv

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    else:
        wb = openpyxl.load_workbook(excelFile)

    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook.
        sheet = wb.get_sheet_by_name(sheetName)

        # Create the CSV filename from the Excel filename and sheet title.
        csvFileName = open(excelFile + sheetName + '.csv', 'w', newline='')

        # Create the csv.writer object for this CSV file.
        csvFile = csv.writer(csvFileName)

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.get_highest_row() + 1):
            rowData = [] # append each cell to this list

            # Loop through each cell in the row.
            for colNum in range(1, sheet.get_highest_column() + 1):
                cellData = sheet.cell(row=rowNum, column=colNum).value
                rowData.append(cellData)

            csvFile.writerow(rowData)

        csvFile.close()
