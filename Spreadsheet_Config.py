import pandas as pd

sheet = pd.read_csv("2 Many Types Spreadsheet - Type Chart.csv")
types = sheet['Unnamed: 0'].tolist()
for t in range(len(types)):
    types[t] = types[t].title().strip()
sheet.index = types
sheet.drop('Unnamed: 0', axis=1, inplace=True)
sheet.columns = types
sheet.to_pickle('Type_Chart_2.pickle')

'''
sheet = pd.read_csv("Too Many Types Spreadsheet - Type Chart.csv")
types = sheet['Unnamed: 1'].to_dict()
sheet.drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 65'], axis=1, inplace=True)
for i in types.keys():
    types[i] = types[i].title()
types[59] = 'OU'
sheet.index = types.values()
sheet.columns = types.values()
for i in sheet.columns:
    sheet[i] = pd.to_numeric(sheet[i])
sheet.to_pickle('Type_Chart.pickle')
'''