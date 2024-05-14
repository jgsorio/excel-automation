import openpyxl

sheet = openpyxl.load_workbook('./example.xlsx')

for sheet_name in sheet.sheetnames:
    rows = list(sheet[sheet_name])
    for row in rows:
        with open('values.txt', 'a') as f:
            f.write(f'{row[0].value} {row[1].value} {row[2].value}\n')
