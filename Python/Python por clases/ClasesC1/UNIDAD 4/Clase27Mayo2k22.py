""" realización del esqueleto del reto 4

    ACLARACIÓN: esta parte del codigo no sera compartido por motivos de posibles inconvenientes de copia y plagio
    si desea ver el contenido de este esquema lo puede consultar el los repositorios github de maestros habilitados
    una vez termine el plazo de entrega de este reto se compartirá el esquema de solución mas no la solución integral
"""

""" continuamos con manipulación de contenedores, en esta ocasión, estudiaremos la función filter
        la función filter, del inglés 'filtrar' como su nombre lo indica, filtra los elementos de un objeto iterable que cumpla con la
        condición asociada
"""
lista = [8,5,4,96,32,15,47]

""" crear una lista con los Numeros pares
"""
#   SOLUCIÓN IMPERATIVA 
lista2 = []
for i in lista:
    if i%2 == 0:
        lista2.append(i)
print(lista2)

#   SOLUCIÓN programación funcional (lambda)
lista2 = list(filter(lambda x: x%2 == 0,lista))
print(lista2)

""" veremos varias formas de recorrer y manipular listas, mas complejas, pero mas cortas y útiles 
"""
lista3 = []
bases = [5,1,4,8,7,3]
for i in range(9):
    lista3.append(i)
print(lista3)

# sintaxis: expresión for i in objeto iterable
lista3 = [i for i in range(9)]  # agrega un elemento 'i' a una lista 10 veces
print(lista3)
lista3 = [i for i in 'Marina']          # agrega cada letra de la cadena como un elemento individual a una lista
print(lista3)
lista3 = [i**2 for i in bases]          # agrega el cuadrado de un elemento base de una lista y lo agrega a una lista 
print(lista3)
lista3 = list(map(lambda x: x**2,bases))# misma función anterior pero incluyendo map y lambda
print(lista3)

""" crear una lista con los números pares del 0 al 50
    programación imperativa
"""
#   SOLUCIÓN IMPERATIVA 
lista4 = []
for i in range(51):
    if i%2 == 0:
        lista4.append(i)
print(lista4)

# sintaxis con if
# sintaxis: expresión for i in objeto iterable if condición

lista5 = [i for i in range(51) if i%2 == 0]
print(lista5)

#   SOLUCIÓN programación funcional (filter y lambda)
lista6 = list(filter(lambda x: x%2==1,range(51)))
print(lista6)

""" localización de valores en un dataframe mediante el método loc
"""
import pandas as pd
import numpy as np
# Crear un data frame a partir de un array numpy
arreglo = np.array([[4,5,2],[4,5,8],[1,4,3]])
print(arreglo)
df0 = pd.DataFrame(arreglo)
print(df0)
# print(df0[1,2]) NO se puede acceder a los valores de un dataframe de la manera convencional, para esto usarelos los metodos loc e iloc
df1 = pd.DataFrame(arreglo, columns=['María','Juan','Tomas'], index=['Enero', 'Febrero', 'Marzo'])
print(df1)
# métodos loc e iloc
print(df1.loc['Enero']) # loc localiza los elementos mediante su indice personalizado
print(df1.iloc[0])      # iloc localiza los elementos mediante el indice base

#   appEnd