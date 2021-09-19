from numpy import column_stack
import pandas as pd

df = pd.read_csv("2020-covid19.csv", encoding = "ISO-8859-1")

df.head(7)
df.tail()
df.shape
df.columns
df['size'].shape

df.describe()

# Creation
df['new_value'] = df['value'] - 10
# Modification
df['value'] = df['value'] - 10
# Data Formatting
df['value'] = int(df['value'])
df['value'] = df['value'].astype('int')

df = df.drop("new_value", axis=1)

df.drop("new_value", axis=1, inplace=True)

# df['COVID-19'] = 
"""
def new_column():
    nliste = []
    liste = df['value']
    for e in liste:
        nliste.append(e/10)
    return nliste
"""

# Indexation

# Acces Colonnes
df[] # 1 column == series
'value'
df[] # 2 columns == dataframe
['value', 'size']
# Acces Lignes
df[1:5]
df[5] # 4 lignes du debut du dataframe
df.iloc[1:5] # 4 lignes du debut du dataframe - iLoc
df.iloc[4] # Acces sur une seule ligne
df.loc # i == index
# Combined Access
df[['value', 'size']][1:10]

# Filtres
df[specificationdecolonnes][df['value'] > 600][1:2]

df[((df['value'] > 600) & (df['value'] < 1000)) | (df['value'] < 1000)]
df[(df['value'] > 600) | (df['value'] < 300)]