# --- FICHIERS EXCEL ---

import openpyxl

wb = openpyxl.load_workbook("octobre.xlsx")
print(wb.sheetnames)
sheet = wb["Feuil1"]
cell = sheet["A1"]
print(cell.value)

print(sheet.max_row)
print(sheet.max_column)


# -- LIRE DE PLUSIEURS FICHIERS ---

wb1 = openpyxl.load_workbook("octobre.xlsx", data_only=True)
wb2 = openpyxl.load_workbook("novembre.xlsx", data_only=True)
wb3 = openpyxl.load_workbook("decembre.xlsx", data_only=True)

def add_data_from_wb(wb, d):
    sheet = wb.active
    for row in range(2,sheet.max_row):
        nom_article = sheet.cell(row=row, column=1).value
        if not nom_article:
            break
        total_ventes = sheet.cell(row, 4).value
        if d.get(nom_article):
            d[nom_article].append(total_ventes)
        else:
            d[nom_article] = [total_ventes]

donnees = {}
add_data_from_wb(wb1, donnees)
add_data_from_wb(wb2, donnees)
add_data_from_wb(wb3, donnees)

print(donnees)