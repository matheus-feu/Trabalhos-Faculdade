import openpyxl

book = openpyxl.load_workbook('Planilha de Compras.xlsx')
frutas_page = book['Frutas']

for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        if cell.value == 'Banana':
            cell.value = 'Abacaxi'

book.save('Planilha de Compras.xlsx')

