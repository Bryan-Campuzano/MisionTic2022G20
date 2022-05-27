""" introducción a operadores lógicos 
"""
#   las tablas de verdad de los operadores entrega el valor de verdad de una operación lógica evaluando el valor
#   de las variables de entrada
#
#   OPERADOR AND
#   A   B   R
#   V   V   V
#   V   F   F
#   F   V   F
#   F   F   F
#
#   OPERADOR OR
#   A   B   R
#   V   V   V
#   V   F   V
#   F   V   V
#   F   F   F
#   A y B indican las variables y R indica el resultado, ejemplo el primer resultado del operador and indica
# 
"""
    Realizar un programa que indique si una persona debe presentar la declaración de renta. 
    Las condiciones para presentar este impuesto son:

    * Ser mayor de edad 

    * Tener ingresos anuales superiores o iguales a $50.831.000
"""
#   SOLUCIÓN A
edadA = int(input("indique su edad: "))
if edadA >= 18: #estructura condicional anidada, se tienen que cumplir ambas condiciones para dar una respuesta afirmativa
    ingresosPA = int((input("indique sus ingresos anuales sin puntos ni comas: ")))
    if ingresosPA >= 50831000:
        print("usted SI debe presentar la declaración de la renta")
    else:
        print("ingresos insuficientes para ser declarante")
else:
    print("edad insuficiente para ser declarante")  
    
#   SOLUCIÓN B
edadB = int(input("indique su edad: "))
if edadB > 17: #usamos mayor estricto porque al tratarse de enteros positivos, el numero mayor mínimo que cumple la condición es 18, que indica mayoría de edad
    ingresosPM = int((input("indique sus ingresos mensuales sin puntos ni comas: ")))#estructura condicional anidada, se tienen que cumplir ambas condiciones para dar una respuesta afirmativa
    if ingresosPM * 12 >= 50831000:
        print("usted SI debe presentar la declaración de la renta")
    else:
        print("ingresos insuficientes para ser declarante")
else:
    print("edad insuficiente para ser declarante")  

#   SOLUCIÓN DE CLASE empleando el operador and
edadC = int(input ("Digite su edad: "))
ingresos=int(input("¿Cuáles son sus ingresos mensuales?"))
ingresoAnual=ingresos*12
if edadC>17 and ingresoAnual >= 50831000: #en esta solución se implementa la condición and, indica que ambas condiciones se deben cumplir para arrojar el primer resultado, si al menos una de las dos es falsa, salta al else
    print("Usted debe presentar la declaración de renta")              
else:
   print("Usted no debe presentar declaración de renta")
 
#   SOLUCIÓN DE CLASE empleando el operador or  
edadD = int(input("Digite su edad: ")) 
ingresos=int(input("¿Cuáles son sus ingresos mensuales?"))
ingresoAnual=ingresos*12
if edadD < 18 or ingresoAnual<50831000:
    print("Usted no debe presentar la declaración de renta")
else:
    print("Usted debe presentar declaración de renta")
    
""" introducción a funciones 
"""
#   Una función es un bloque de código que realiza alguna operación
#   Una función puede definir opcionalmente parámetros de entrada que permiten a los llamadores pasar argumentos a la función
#   Una función también puede devolver un valor como salida
#
#   los micro-códigos hechos en anteriores clases se pueden considerar como funciones, mas sin embargo, en programación se
#   tienen que definir como tal, para permitirle al programador y al programa el "llamar" a estas funciones de manera
#   independiente sin necesidad de ejecutar todo el código, y volver a usar piezas de código en otros sectores
#
#   las funciones se definen con el comando "def"

def saludo():
    print("Hola Mundo, mi nombre es Bryan")

saludo() 

def suma (num1,num2): #las funciones pueden tener parámetros, estos son valores de inicio dados por el usuario o por otras funciones que la función actual requiere para hacer su tarea
    return num1+num2

suma(15,20)

#   appEnd