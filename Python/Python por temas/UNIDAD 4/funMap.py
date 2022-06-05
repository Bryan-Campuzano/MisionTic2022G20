# sintaxis:
# map(función, objeto iterable)
# develve un objeto map
from math import pow
from functools import reduce
lista = [5,8,2,9,3,6]

# realice un programa que cree una nueva lista donde cada elemento
# sea el cuadrado de los elemento de "lista"

# programación imperativa
lista2 =[]
for i in lista:
    lista2.append(i**2)
print(lista2)

# programación funcional, utilizando map y funciones
def cuadrados(num):
    return num**2 
lista2 = list(map(cuadrados, lista))
print(lista2)

# programación funcional, utilizando lambda y map
lista2 = list(map(lambda x: x**2,lista))
print(lista2)

# Genera una lista cuyos elementos sean x**y, donde x son los elementos de "bases"
# y y son los elemntos de "potencias"
bases = [5,1,2,7,4]
potencias = [1,3,4,0,5]
lista2 = list(map(pow,bases,potencias))
print(lista2)

lista = [
    [1525, [4, 2500],[3,8500],[5,12600]], #[No. factura, [cantidad, precio unidad], ...[]]
    [1520, [3, 2500],[8,12600]],
    [1622, [1, 2500],[5,8500],[2,12600]]    
]

#Crear una nueva lsta que tega la siguiente forma:
# [[codigo de la factura, total1, total2,... totaln], [],...[]], total1, es cantida por precio unidad

lista2 = list(map(lambda x: [x[0]]+list(map(lambda y: y[0]*y[1] ,x[1:])) ,lista))
print(lista2)

#crear una nueva lista de la forma:
#[[codigo de la factura, total factura], []...[]]
lista2 = list(map(lambda x: [x[0]]+ [reduce(lambda a,e: a+e,x[1:])],lista2))
print(lista2)

#Si la compra total es mayor o igual a 100.000 pesos, se gana un bono de 5000
#Crear una lista iagual a la anterior,pero que tenga el bono incluido

#[[1525, 98500], [1520, 108300], [1622, 70200]]
lista2 = list(map(lambda x: x if x[1] < 100000 else [x[0]]+[x[1]-5000],lista2))
print(lista2)





