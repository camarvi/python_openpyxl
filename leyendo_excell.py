import openpyxl

book = openpyxl.load_workbook('prueba_escribir.xlsx')

sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']

print(a1.value)
print(a2.value)


# Ver el tipo de dato
print(type(a1.value))
print(type(a2.value))

#Acceder a otra hoja
sheet2 = book['hoja_2']
a1 = sheet2['A1']
print(a1.value)