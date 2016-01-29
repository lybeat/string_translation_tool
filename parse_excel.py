import xdrlib, sys
import xlrd

def open_excel(file):
	try:
		data = xlrd.open_workbook(file)
		return data
	except(Exception, e):
		print(str(e))
	else:
		pass
	finally:
		pass

def excel_table_by_index(file, col_name, index):
	data = open_excel(file)
	table = data.sheets()[index]
	nrows = table.nrows
	ncols = table.ncols
	print('nrows: ' + nrows)
	row_values = table.row_values(col_name)
	lists = []
	for nrow in range(1, nrows):
		row = table.row_values(nrow)
		if row:
			app = {}
			for i in range(len(row_values)):
				app[row_values[i]] = row[i]
			lists.append(app)
	return lists

def main():
	tables = excel_table_by_index('test.xls', 0, 0)
	print('hello world')
	for row in tables:
		print(row)
	if __name__=="__main__":
		main()
