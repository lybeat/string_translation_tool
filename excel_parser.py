# -*- coding: utf-8 -*-
import xlrd
# import xlwt
from datetime import date,datetime
 
def read_excel():
  # 打开文件
  workbook = xlrd.open_workbook('test.xls')
  # 获取所有sheet
  print workbook.sheet_names() # [u'sheet1', u'sheet2']
 
if __name__ == '__main__':
  read_excel()