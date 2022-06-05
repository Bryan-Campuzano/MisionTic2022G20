lista = [8,5,4,96,32,15,47]
#crear una lista con los numeros pares
#programación funcional
lista2 = []
for i in lista:
    if i%2 == 0:
        lista2.append(i)
print(lista2)
#programacion funcional con lambda
lista2 = list(filter(lambda x: x%2 == 0,lista))
print(lista2)