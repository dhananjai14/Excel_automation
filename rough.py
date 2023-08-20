import pandas as pd
from src.entity import entity_artifact


df = pd.read_excel(r'D:\DS\Project\ExcelAutomation\Sample_Input\Input.xlsx', None)

sheet_lst = list(df.keys())
print(sheet_lst)