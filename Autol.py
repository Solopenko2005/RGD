import openpyxl
import pandas as pd
ws = pd.read_excel('C:/Users/User/Desktop/МДТ/1.xlsx')
ws_np = np.array(ws)

# Сохранить файл
wb.save("sample.xlsx")