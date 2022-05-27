""" introducción a los conjuntos
"""
#   los conjuntos son colecciones de datos en las cuales se almacenan varios elementos
#   no están ordenados, son inmutables y no permiten valores duplicados

conjunto = {'Cali','Barranquilla','Bucaramanga'}    # la notación de los conjuntos es similar a la de los diccionarios, pero sin parámetros, se almacenan unicamente los valores
print(type(conjunto))                               # esto imprime en consola el mensaje "<class 'set'>" que indica que es un conjunto
print(conjunto)

conjunto2 = {2,4,5,3,3,3,7,9}                       # no contempla los elementos repetidos, en este caso retornara solo un 3
print(conjunto2)

conjunto3 = {3,5.0,True,'Carlos',[1,2,3]}           # puede almacenar elementos de varios tipos, mientras estos sean inmutables
print(conjunto3)                                    # retorna un error de "unhashable type: list" que indica que es un elemento incompatible con los conjuntos

conjunto4 = set((3,7,(9,8,7)))                      # en este caso si que retorna todos los elementos pues las tuplas son inmutables
print(conjunto4)                                    # para asignarle directamente el valor de "set" a un grupo de elementos, en vez de los corchetes, se usa doble paréntesis

conjunto3.add('Pedro')                              # se pueden añadir y quitar elementos
conjunto3.remove(5.0)                               # retorna el conjunto modificado

""" operaciones con conjuntos
"""
carbohidratosNat = {'papa','yuca','ñame','pan'}
carbohidratosProc ={'Harina de trigo','Pasta','pan'}
"""     operadores de conjuntos:

        | representa union
        & representa intersección
        - representa Diferencia
        ^ representa diferencia simétrica
"""
print('--------------caracteres------------------')
print(carbohidratosProc|carbohidratosNat)           # aquí se imprimen los resultados de las operaciones básicas de conjuntos
print(carbohidratosProc&carbohidratosNat)
print(carbohidratosProc-carbohidratosNat)
print(carbohidratosProc^carbohidratosNat)
print('---------------funciones------------------')
print(carbohidratosProc.union(carbohidratosNat))    # también existen estas operaciones básicas en su forma de función en la clase de conjuntos "set"
print(carbohidratosProc.intersection(carbohidratosNat))
print(carbohidratosProc.difference(carbohidratosNat))
print(carbohidratosProc.symmetric_difference(carbohidratosNat))

print(len(carbohidratosNat))                        # también se puede contar la cantidad de elementos existentes en el conjunto

lista = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]       # creo una lista con elementos repetidos, que se pueden recorrer
conjunto1 = set(lista)                              # creo un conjunto con estos elementos
print(conjunto1)                                    # como no admite elementos repetidos, solo me retorna una cadena con los valores sin sus duplicados
#   appEnd