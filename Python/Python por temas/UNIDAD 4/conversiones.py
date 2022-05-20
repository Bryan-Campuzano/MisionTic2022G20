#Conversión de cadena a lista
cadena = 'Colombia'
lista = list(cadena)
print(lista)

#Conversión de lista a cadena
cadena2= ''.join(lista)
print(cadena2)

lista2 = [1,5,8,7,3]
# cadena3 = ''.join(lista2), NO se puede porque join requiere que los elementos
# sean str.

#Conversión de listas a conjuntos
conjunto = set(lista)
print(conjunto)

#Conversion de cadena a diccionario
diccionario = dict(zip(range(len(cadena)),cadena))
print(diccionario)
# range de 10(0-9)
tempo = list(zip(range(len(cadena)),cadena))
print(tempo)

#Conversión desde diccionarios
#diccionario.keys(), diccionario.values(), diccionario.items()
print(diccionario.keys())
print(diccionario.values())
print(diccionario.items())
cadena3 = ''.join(diccionario.values())
print(cadena3)


