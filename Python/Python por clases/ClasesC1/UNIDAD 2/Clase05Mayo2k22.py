"""  continuacion del tema de funciones
"""

"""  esta funcion hace una resta de dos números dados, num1 y num2 son parametros de entrada
"""
def resta(num1, num2):
    return num1-num2

print(resta(10,8)) #el llamado de la funcion esta dentro del print

"""  esta funcion ejecuta una de cuatro operaciones matemáticas básicas  dependiendo la seleccionada por el usuario
     num1, num2 y operador son parametros de entrada de la funcion
"""

#    SOLUCIÓN A
def operaciones(a,b,operador):     #se introducen dos números y un operador que indica que operacion matemática se ha de realizar
    if operador == "+":            #se compara el operador introducido con el operador de este caso individual
         return a+b                #de ser igual, ejecuta la operacion indicada, en este caso, la suma
    elif operador == "-":          #aquí se usa un nuevo condicional llamado elif, es la fusion de un else y un if, en otras palabras si el condicional original es falso y salta al else, se evalúa otra condición inmediatamente.
         return a-b
    elif operador == "*":
         return a*b
    elif operador == "/":
         return a/b
    else:
        return print("Digite un operador valido")

#    SOLUCIÓN B
def operaciones2(a,b,operador):    #se introducen dos números y un operador que indica que operacion matemática se ha de realizar
    if operador == "+":            #se compara el operador introducido con el operador de este caso individual
         resultado = a+b           #de ser igual, ejecuta la operacion indicada, en este caso, la suma
    elif operador == "-":          #aquí se usa un nuevo condicional llamado elif, es la fusion de un else y un if, en otras palabras si el condicional original es falso y salta al else, se evalúa otra condición inmediatamente.
         resultado = a-b
    elif operador == "*":
         resultado = a*b
    elif operador == "/":
         resultado = a/b
    else:
        resultado = "Digite un operador valido"
    return resultado

print("___________________________")
print(operaciones (5,8,"+")) #este es un test de todos los casos de la funcion operaciones
print(operaciones (5,8,"-"))
print(operaciones (5,8,"*"))
print(operaciones (5,8,"/"))
print(operaciones (5,8,"p"))
print("___________________________")
print(operaciones2 (5,8,"+")) #este es un test de todos los casos de la funcion operaciones2
print(operaciones2 (5,8,"-"))
print(operaciones2 (5,8,"*"))
print(operaciones2 (5,8,"/"))
print(operaciones2 (5,8,"p"))
print("___________________________")

"""  introducción a cadenas avanzadas
"""

"""  esta funcion imprime en consola información básica dada
"""
print("Hola mundo")
nombre="Marina" 
edad=45
ciudad="Medellin"
print(nombre, "vive en",ciudad, "y tiene", edad, "años") #aquí vemos una concatenacion de elementos de diferentes tipos 

"""  esta funcion imprime en consola información básica dada con f-string
"""
print(f"{nombre} vive en {ciudad} y tiene {edad} años") #aquí se introduce un nuevo tipo de concatenacion llamada f-string, una cadena en la que se pueden agregar parametros dentro de un string haciendo parte de la cadena 

"""  esta funcion imprime en consola información básica dada con string.format()
"""
print("{0} vive en {1} y tiene {2} años".format(nombre,ciudad, edad)) #este tipo de string funciona similar a una funcion estándar, pues se declara donde van a ir los parametros y al final se hace un llamado a la función .format() donde se introducen los parametros en orden

"""  introducción a Booleanos 
"""

"""  funcion de prueba de variables booleanas y sus operadores
"""
a = True #las variables booleanas solo pueden tener dos estados, verdadero o falso, operando estas variables
b = False

print(a,b)
print(type(a), type(b))
print(not(a), not(b))    #la funcion "not" niega la variable introducida, si esta es verdadera, al ser negada pasa a ser falsa (si a = True, entonces, not(a) = false y biceversa)
print(5>8)               #estas expresiones son expresiones booleanas, pues el resultado de la expresion "5>8" es un booleano
print(8>5)

"""  esta funcion enciende una alarma cuando una puerta o una ventana o ambas están abiertas

Parámetros:    sensorPuerta(bool): booleano que indica si la puerta esta abierta (true: abierta, false: cerrada)
               sensorVentana(bool): booleano que indica si la ventana esta abierta (true: cerrada, false: abierta)
retorna:       String: de la forma "alarma encendida/apagada"
"""
#   tabla de verdad de la funcion alarma
#
#   OPERADOR or : A = ventana, B = puerta
#   not(A)  B   R
#   V       F   V
#   F       F   F * la única combinación falsa es en la que tanto ventana como puerta están cerradas, en cualquier otro caso, se activa la alarma
#   V       V   V
#   F       V   V
#
ventana =True
puerta =False
if puerta or not(ventana):
    print("alarma encendida")
else:
    print("alarma apagada")
    
#    appEnd