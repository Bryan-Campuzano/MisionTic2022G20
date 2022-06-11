import pandas as pd
df1 = pd.read_csv('surveys.csv')
print(df1.head(15)) # imprime las primeras 15 filas
print(df1.tail(15)) # imprime las ultimas 15 filas
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['species_id'])) # imprime una lista de los datos únicos de la columna
print(df1['species_id'].value_counts()) #cuenta los datos únicos de la columna
print(df1['weight'].describe()) #descripción, muestra un resumen de datos de estadistica descriptiva
print(df1['weight'].mean()) #Me arroja un promedio del peso
datosGrupoSexo = df1.groupby('sex') # Creamos un grupo
print(datosGrupoSexo.describe()) #obtenemos información del grupo
print(datosGrupoSexo.max())
print(df1.groupby('species_id')['record_id'].count()['NL'])





