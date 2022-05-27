""" continuamos con el tema de contenedores, en esta ocasión vamos a ver diferentes formas de convertir
    estos contenedores en otros, manteniendo y manipulando el contenido a necesidad
"""
"""Conversión de cadena a lista
"""
cadena = 'Colombia'     # elemento en forma de cadena: 'Colombia'
lista = list(cadena)    # elemento en forma de lista: ['C', 'o', 'l', 'o', 'm', 'b', 'i', 'a']
print(lista)            # el resultado es una lista indexada con los elementos de la cadena original separada en cada posición

""" Conversión de lista a cadena
"""
cadena2= ''.join(lista) # el comando join permite concatenar indefinida cantidad de strings y retorna como resultado
print(cadena2)          # una cadena nueva juntando todos los valores en orden. en este caso, agrega todos los valores
                        # de la lista, uno tras otro, en el orden dado por la propia lista

lista2 = [1,5,8,7,3]    # esta lista no se puede concatenar con el comando join pues no son elementos de tipo str

"""Conversión de listas a conjuntos
"""
conjunto = set(lista)   # agrega los elementos de la lista en un conjunto, pero como es un contenedor no indexado
print(conjunto)         # a la hora de solicitar los elementos, se retornaran en un orden aleatorio

"""Conversion de cadena a diccionario
"""
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)

#   appEnd