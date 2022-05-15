# las tuplas son colecciones de datos que se utilizan para almacenar varios datos
# colección ordenada y son inmutables
# colección indexada numéricamente

fruta = ('manzana', 'pera', 'piña')
print(fruta)
print(fruta[1])
# fruta[0]='papaya' esto no se puede porque las tuplas son inmutables
print(type(fruta))
animales = ('perro',)
print(animales)
print(type(animales))
tupla = ('Carlos', 20, True, 45.9, [3,5,2])
print(tupla)
lista = list(tupla)
print(lista)
lista[0]='Laura'
tupla = tuple(lista)
print(tupla)
print(lista)

def operaciones(a,b):
    suma = a + b
    resta = a- b
    mul = a*b
    div = a/b
    sw = True
    return suma,resta,mul,div, sw


print(operaciones(4,2))
a = operaciones(4,2)
print(type(a))

dulces = tuple((1258,2))
print(dulces)
print(type(dulces))