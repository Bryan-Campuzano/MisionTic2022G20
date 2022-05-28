# sintaxis: reduce(función, obejto iterable)
# se debe importar reduce de la librería functools
from functools import reduce

lista = [5,2,7,8]
def acumular(acumulador, elemento):
    return acumulador + elemento
total= reduce(acumular, lista)
print(total)

#programación funcional con reduce y lambda

total = reduce(lambda a,e: a + e, lista)
print(total)