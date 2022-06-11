import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1.columns)
print(df1['month']) # subconjunto de columnas
print(df1.month)
df2 = df1.month
print(type(df1), type(df2))
df2 = df1[['species_id','plot_id']] #subconjunto de varias columnas
print(df2)
print(df1[10:21]) # subconto de filas y columnas
print(df1.iloc[0:4,1:3])
print(df1.iloc[[0,4,7],:])
print(df1.iloc[4,2])
print(df1[df1.year==1977]) # filtro de filas según un criterio
print(df1[(df1.year >= 1985) & (df1.year <=1995)]) #and: &, or: |, not:~
