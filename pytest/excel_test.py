import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title = "ceshi.xlsx"
sheet['C3'] = 'Hello world!'
wb.save('testexcel.xlsx')
