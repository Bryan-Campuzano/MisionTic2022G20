#Realice un programa que detecte si un numero es par o no
numero = int(input("Digite el número\n"))
#módulo de dos numeros arroja el residuo de la división
#ejemplo 9 módulo 3 es igual a 0
#ejemplo 8 módulo 3 es igual a 2
#El operador del módulo en python es el %
if numero%2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# operadores:
# Aritméticos: + - * / % ** //
# 5**2 = 25 potencia
# 18//4 = 4 división con resultado entero
# Relacionales: < <= > >= == !=(diferente)
# Lógicos: and or not
