import openpyxl


header = ['id', 'name', 'age']
wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(header)
data = (
    (1, 'Guilherme', 33),
    (2, 'Ana', 29),
    (3, 'Rute', 25)
)


for item in data:
    sheet.append(item)

total_data = len(data) + 1
sheet.append(['Total', '', f'=SUM(C2:C{total_data})'])

wb.save('./users.xlsx')