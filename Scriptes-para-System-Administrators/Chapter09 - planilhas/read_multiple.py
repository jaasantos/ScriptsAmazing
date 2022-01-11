import openpyxl

book_obj = openpyxl.load_workbook('test.xlsx')

excel_sheet = book_obj.active

cells = excel_sheet['A1': 'C6']

for c1, c2, c3 in cells:
	print(f"{0:6} {1:6} {2:6}".format(c1.value, c2.value, c3.value))

