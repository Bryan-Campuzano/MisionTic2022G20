import pandas as pd
import numpy as np
# Crear un data frame a partir de un array numpy
arreglo = np.array([[4,5,2],[4,5,8],[1,4,3]])
print(arreglo)
df0 = pd.DataFrame(arreglo)
print(df0)
# print(df0[1,2]) NO se puede
df1 = pd.DataFrame(arreglo, columns=['María','Juan','Tomas'], index=['Enero', 'Febrero', 'Marzo'])
print(df1)
# métodos loc e iloc
print(df1.loc['Enero'])
print(df1.iloc[0])




