import openpyxl

book = openpyxl.load_workbook('prueba_escribir.xlsx')

sheet = book.active

sheet['E1']='Suma Total'
sheet['E2']='=SUM(B2:B14)'

book.save('prueba_escribir.xlsx')
