""" este archivo esta creado con la finalidad de que puedas extraer partes de código especificas, ejecutarlas,
    modificarlas,etc.
"""

#------------------------ZONA DE CÓDIGO------------------------
""" introducción a las listas
"""
MarcasCarros = ['Audi','Chevrolet','Renault','Toyota']  # a diferencia de los diccionarios, la notacion de las listas se hace con "[]" en vez de corchetes
datosPersonales = ['Carlos', 40, True]                  # no hay que guardar sus elementos dentro de keys o parametros, solo se guardan los valores a usar
print(MarcasCarros)                                     # puede contener valores de diferentes tipos, cadenas, enteros etc
print(datosPersonales)

frutas = list(('manzana','pera','fresa'))
print(frutas)
frutas[2]='piña'
print(frutas)

for i in frutas:
    print(i)
#-------------------------ZONA DE TEST-------------------------




#appEnd