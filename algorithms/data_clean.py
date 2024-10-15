import pandas as pd
file_path = 'data/NJIT ICORPS NATIONAL AWARDS.xlsx'
df = pd.read_excel(file_path, skipfooter=11) # skipfooter = skip last 11 lines b/c its random notes
print(df)
