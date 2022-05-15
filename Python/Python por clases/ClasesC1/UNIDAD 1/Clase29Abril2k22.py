""" esta funcion toma dos concatenaciones y devuelve la suma de estas.
"""
saludo1 = "hola mundo"
nombre = "Mi nombre es Bryan"
saludo2 = saludo1+" "+nombre #concatenacion de variables de tipo string
print (saludo2) 

""" esta funcion toma dos números dados por el usuario y devuelve la suma de estos.
"""
a=input("Digite el número 1: ") #formulario de entrada de información numero 1
b=input("Digite el número 2: ") #formulario de entrada de información numero 2
c=int(a)+int(b)                 #suma de números dados por el usuario
print(c)                        #retorna la suma de los números dados en terminal

""" introducción a los condicionales 
"""

""" esta funcion lee un numero he indica si este es mayor igual a 100.
"""
numero = input ("Digite el numero: ") #numero introducido por el usuario. numero es de tipo string
numero2 = int(numero)                 #toma el numero tipo string y retorna un int
if numero2 >= 100:                    #condición de evaluación
    print ("el "+numero+" es mayor a 100") #retorna un mensaje si numero2 es mayor a 100
else: 
    print("el "+numero+" es menor a 100") #retorna un mensaje alternativo si numero2 es menor a 100

""" introducción a los ciclos  
"""  

""" funcion que cuenta de 1 a 10 (ciclos tipo while).
"""  
contador=1                  #se inicializa una variable de tipo int que servira como indice del ciclo
while contador <=10:        #este ciclo se repetirá hasta que la condición (el contador sea menor o igual a 10) deje de cumplirse, mientras sea verdadera, el código posterior se repetirá  
   print(contador)          #imprime el valor actual de la variable contador en pantalla
   contador = contador+1    #aumenta en 1 el valor de la variable contador
   
""" funcion que cuenta de 1 a 10 (ciclos tipo for).
""" 
for contador in range(10):
    print (contador)

""" pruebas para ver el comportamiento de las variables en un ciclo.
"""
for contador in range(1,10): #se agrega la condición de ciclo finito, empieza por 1 y termina cuando la variable contador sea igual a 10
    print (contador)
    
for contador in range(0,11): #se cambia el punto de partida
    print (contador)
    
for contador in range(0,10,2): #se agrega una condición extra, la medida del aumento, este tercer indicador dictamina en que medida se incrementa el contador, en este caso, cada iteración suma dos unidades a contador
    print (contador)
    
""" esta funcion dice si un número entero dado e indica si este es mayor o igual a 100 reiteradas veces hasta que el usuario dictamine.
"""
respuesta = 'S'
while respuesta == 'S':                 #esta condición se cumple dependiendo de la decision del usuario
    numero=input("Digite el número: ")  #a variable numero se dictamina por el usuario, la variable esta dentro del while porque se requiere una respuesta por cada iteración
    if int(numero) >= 100:              #compara la variable numero con el entero 100, 
        print("El número es mayor o igual a 100") #imprime en consola el mensaje determinado si numero es mayor que el entero 100      
    else:
        print("El número es menor a 100") #en caso de que la variable numero no sea mayor que el entero 100, entonces imprime en consola un mensaje diferente
    respuesta =input('Digite "S" para continuar, cualquier otra tecla pasa salir') #nótese que la variable respuesta esta al mismo nivel de identacion que el if y el else, esto es porque quiero que se evalúe dentro del ciclo while al mismo nivel que las otras condiciones 
     
""" esta funcion dice si un numero dado por el usuario es par o impar
"""
num=int(input ())
if num<0:
    print ("El número debe ser positivo")
else:
    if int(num/2)*2 == num:
        print("El numero es par")
    else:
        print("El número no es impar")
#NOTA SOBRE ESTA FUNCION: en el segundo if, matemáticamente es un error, pues el dividir y multiplicar 
#por el mismo numero un entero, da como resultado este mismo entero. mas sin embargo, al estar num/2 dentro de
#la funcion int, esta lo convertira en el entero mas proximo a la baja, cambiando el valor de los impares y 
#conservando el de los pares, pues estos al ser divididos no adquieren una parte decimal, conservando su valor.
#EJEMPLO: num=3, num/2= 1.5, int(1.5)= 1, 1*2=2, 3 es diferente de 2, por ende, 3 es impar.

#   appEnd