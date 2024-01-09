#LER E ALTERAR DADOS DE UMA PLANILHA

from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'workbook.xlsx'   

#Carregando um arquivo do excel
workbook: Workbook = load_workbook(WORKBOOK_PATH)

sheet_name = 'Minha_planilha'

worksheet: Worksheet = workbook[sheet_name]


row: tuple[Cell]
for row in worksheet.iter_rows():
    for cell in row:
        print(cell.value, end='\t')
    
        if cell.value == 'Maria': 
            worksheet.cell(cell.row, 2, 23)
    print()

worksheet['B4'].value = 12 # para mudar valor na planilha

workbook.save(WORKBOOK_PATH)