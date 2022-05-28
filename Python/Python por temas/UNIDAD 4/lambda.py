# Función lambda o función anónima 
# Función que solo contiene una instrucción, es una instrucción de una línea
# Sintaxis de lambda:
# lambda argumentos: cuerpo de la función

tempo = lambda a: a**2
print(tempo(5))
print(tempo(10))
print(tempo(6))

def operaciones(a,b, fn):
    return fn(a,b)

suma = operaciones(10,9, lambda x, y: x+y)
print(suma)
resta = operaciones(10,9, lambda x, y: x-y)
print(resta)
