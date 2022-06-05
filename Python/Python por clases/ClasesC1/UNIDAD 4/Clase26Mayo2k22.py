""" introducción a la función map y sus utilidades
"""

"""
    map lo que hace sobre un objeto iterable (listas, tuplas, etc.) recorrer todos sus elementos y a cada
    uno efectuar un método
    sintaxis:
        map(función, objeto iterable)
    devuelve un objeto (iterable) map con los resultados de la función efectuada en todos los elementos, este objeto no se puede
    imprimir asi que tiene que ser almacenado primeramente como objeto iterable 
"""
#------------------IMPORTACIONES-----------------
from math import pow    
from functools import reduce

""" realice un programa que cree una nueva lista donde cada elemento
    sea el cuadrado de los elemento de "lista"
"""
lista = [5,8,2,9,3,6]
# SOLUCIÓN 1: programación imperativa
lista2 =[]
for i in lista:
    lista2.append(i**2)
print(lista2)

# SOLUCIÓN 2: programación funcional, utilizando map y funciones
def cuadrados(num):
    return num**2 
lista2 = list(map(cuadrados, lista))
print(lista2)

# SOLUCIÓN 3: programación funcional, utilizando lambda y map
lista2 = list(map(lambda x: x**2,lista))
print(lista2)

""" Genera una lista cuyos elementos sean x**y, donde x son los elementos de "bases"
    y y son los elementos de "potencias" 
"""
bases = [5,1,2,7,4]
potencias = [1,3,4,0,5]
lista2 = list(map(pow,bases,potencias)) # el método pow retorna la potencia de x^y donde X es la base y Y la potencia
print(lista2)

""" Crear una nueva lista que tenga la siguiente forma:
        [[codigo de la factura, total1, total2,... totaln, [],...[]]]
    total1, es el precio total (cantidad * precio unitario)
"""
#   EXPLICACIÓN DEL MÉTODO:
#   tenemos una lista de listas. cada elemento de la lista principal es una lista que representa una factura
#   con un numero de ID y una serie de subtotales (parejas de valores necesarios para dar un total)
#   si pasamos de llamar a 'lista' a llamarla x, tenemos que cada elemento de esta lista se puede identificar como
#   x[a] siendo 'a' un entero que indica la posición (x[0] es el primer elemento, x[1] el segundo...)
#   el método nos solicita que tomemos cada pareja de subtotales y la multipliquemos para obtener el valor final
#   para esto partimos cada elemento x en dos partes, por una parte los elementos x[0] de cada factura, pues son los ID
#   y no es necesario operarlos, pero los necesitamos para identificar a donde pertenecen las parejas de subtotales.
#   para este fin usamos el primer map, encargado de separar los ID de los subtotales. ahora necesitamos recorrer
#   la segunda 'porción' de cada factura, y multiplicar los subtotales con sus respectivas parejas, para esto necesitamos
#   recorrer estas porciones con un segundo map, que recorre desde x[1] hasta el final, toma cada pareja como una lista secundaria
#   a la cual denominamos 'y', entonces recorrerá cada porción de x, tomara cada pareja de y, la multiplicará y la sumará al ID
#   recordemos que la 'suma' de listas es una concatenación, entonces a cada ID se le irá asignando nuevos elementos con los valores totales  

lista = [
    [1525, [4, 2500],[3,8500],[5,12600]], #[No. factura, [cantidad, precio unidad], ...[]]
    [1520, [3, 2500],[8,12600]],
    [1622, [1, 2500],[5,8500],[2,12600]]    
]
lista2 = list(map(lambda x: [x[0]]+list(map(lambda y: y[0]*y[1] ,x[1:])) ,lista))
print(lista2)

""" explicación de la función 'reduce'
        la función 'reduce' suma los elementos de un objeto iterable de manera acumulativa
    sintaxis: reduce(función, objeto iterable)
        ejemplo: reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calcula ((((1+2)+3)+4)+5)
        
"""
from functools import reduce        # se debe importar reduce de la librería functools

lista = [5,2,7,8]                   # tenemos una lista base
def acumular(acumulador, elemento): # creamos una función que suma dos valores dados
    return acumulador + elemento
total= reduce(acumular, lista)      # el propósito de 'reduce' es tomar todos los argumentos y reducirlos a un único valor mediante operaciones aritméticas
print(total)

#solución con programación funcional (reduce y lambda)

total = reduce(lambda a,e: a + e, lista)
print(total)

""" crear una nueva lista de la forma:
        [[codigo de la factura, total factura], []...[]] 
    donde el total factura es la suma de todos los valores ya procesados
"""
lista2 = list(map(lambda x: [x[0]]+ [reduce(lambda a,e: a+e,x[1:])],lista2))   
print(lista2)                                                                   

#   NUEVO REQUERIMIENTO: Si la compra total es mayor o igual a 100.000 pesos, se gana un bono de 5000

""" Crear una lista igual a la anterior,pero que tenga el bono incluido
"""
#ESTADO ACTUAL DE lista2: [[1525, 98500], [1520, 108300], [1622, 70200]]
lista2 = list(map(lambda x: x if x[1] < 100000 else [x[0]]+[x[1]-5000],lista2)) #aunque es un poco contra-intuitivo, la condición se efectúa en el 'else' y en el 'if' no hace nada 
print(lista2)

#   appEnd