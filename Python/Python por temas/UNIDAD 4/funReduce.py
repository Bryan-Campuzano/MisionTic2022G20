# sintaxis: reduce(función, objeto iterable)
# se debe importar reduce de la librería functools
from functools import reduce

lista = [5,2,7,8]                   # tenemos una lista base
def acumular(acumulador, elemento): # creamos una función que suma dos valores dados
    return acumulador + elemento
total= reduce(acumular, lista)      # el propósito de 'reduce' es tomar todos los argumentos y reducirlos a un único valor
print(total)

#programación funcional con reduce y lambda

total = reduce(lambda a,e: a + e, lista)
print(total)