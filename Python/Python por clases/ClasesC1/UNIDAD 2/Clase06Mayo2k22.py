""" profundización en temas vistos anteriormente
"""
""" esta funcion evalúa cual es el numero mayor de una lista de números dados por el usuario
"""
cantidadNum= int(input("Digite la cantidad de números que va a ingresar: \n")) #la expresion \n es sencillamente un salto de linea, en vez de solicitar el numero en la misma linea, lo hace en una linea mas abajo, es como presionar la tecla enter
for i in range(1, cantidadNum + 1):                                            #ciclo que comienza desde el primer elemento y finaliza en cantidadNum+1, esto es porque el conteo de un for inicia normalmente en cero, entonces el indicador del formulario f"ingrese el numero {i}\n" iniciaria de la forma "ingrese el numero 0" es meramente estético
   numero = int (input(f"ingrese el numero {i}\n"))                            #NOTA: el rango puede iniciar del numero que se quiera, y terminar en cualquier numero posterior, solo hay que tener en cuenta el tamaño del conteo, si queremos 5 iteraciones, podemos ir de 0 a 4, de 1 a 5, de 2 a 6 etc. esto para evitar tener iteraciones insuficientes o innecesarias
   if i==1:
       mayor = numero
   elif numero>mayor:
            mayor= numero
print(f"El mayor de los {cantidadNum} números ingresados es {mayor}")

""" esta funcion evalúa cual es el numero menor de una lista de números dados por el usuario
"""
#cambia la condición de evaluación, el nombre de ciertas variables y el string de salida, de resto es una funcion muy similar
cantidadNum2= int(input("Digite la cantidad de números que va a ingresar: \n"))
for i in range(1, cantidadNum2 + 1):
    numero2 = int (input(f"ingrese el numero {i}\n"))
    if i==1:
       menor = numero2
    elif numero2<menor: 
            menor= numero2
print(f"El menor de los {cantidadNum2} números ingresados es {menor}")

""" esta funcion evalúa cual es el numero menor y mayor de una lista de números dados por el usuario
"""
cantidadNum3 = int(input("Digite la cantidad de números que va a ingresar: \n")) #el cambio del nombre de las variables es solo para evitar que la funcion actual tome las variables temporales declaradas en funciones anteriores y las use en esta funcion
for i in range(1, cantidadNum3 + 1):
    numero3 = int(input(f"ingrese el numero {i}\n"))
    if i==1:
       menor2 = numero3
       mayor2 = numero3
    else:
        if numero3 > mayor2: 
            mayor2 = numero3
        if numero3 < menor2:
            menor2 = numero3
print(f"El mayor de los {cantidadNum3} números ingresados es {mayor2}")
print(f"El menor de los {cantidadNum3} números ingresados es {menor2}")

""" Realice un ejercicio que convierta notas de 1 a 5, con un decimal a letras según la siguiente tabla:
    
    1 a 2.9 =>D
    3 a 3.5 =>R
    3.6 a 4 =>B
    4.1 a 5 =>E
    
"""
nota = float(input (f"Digite la nota numérica que desea convertir\n"))
if  nota  > 1 and nota < 3:
    letra = "D"
elif nota >=3 and nota < 3.6:
    letra = "R"
elif nota > 3.6 and nota <= 4:
    letra = "8"
elif nota > 4 and nota <= 5:
    letra = "E"
else:
    print("Digite una nota válida")
    letra = "invalida" #este valor de letra se asigna para que en el caso de que la nota sea invalida, el print final no arroje error, pues la variable letra solo existe dentro de los elif
print(f"la nota es {letra}")

""" Diseñe un algoritmo para calcular la longitud de la hipotenusa
    (es decir, el lado más largo de un triángulo rectángulo,el opuesto al ángulo recto) 
    utilizando el Teorema de Pitágoras:
    
    C = √(a^2+b^2)
"""
def hipotenusa (a,b):
    h = (a**2 + b**2) ** 0.5 #el operador ** indica potencia en python
    return h
print(hipotenusa(4,5))

""" funcion para la profundización en cadenas
"""
animal = "cocodrilo"
print(animal[2])     #retorna la letra ubicada en la posición 2 de la cadena, como siempre, iniciando la cuenta desde cero 

print(animal[-2])    #también se puede solicitar una posición negativa que no es mas que recorrer de derecha a izquierda la cadena empezando desde la posición 0, en este caso saltando a la "o final" y despues a la ultima "l"

print(animal[0:3])   #en este caso podemos retornar fragmentos de la cadena mas grandes, por ejemplo de 3 letras especificas

print(animal[:4])    #retorna la fracción de la cadena de la posición 0 hasta la posición 4 

print(animal[4:])    #retorna la fracción de la cadena de la posición 4 hasta el final de la cadena 

print(len(animal))   #retorna el tamaño de la cadena, siendo este la cantidad de letras

print("coc" in animal) # retorna true si la cadena dada se encuentra como sub-cadena de una cadena mayor, false de lo contrario. en este caso, busca la sub-cadena "coc" en la cadena animal, retornando true pues si existe como fracción de "cocodrilo"

for i in range(len(animal)):
    print(animal[i])    #recorre la cadena, e imprime letra por letra en consola
    
for i in animal:
    print(i)            #en esta version de la misma funcion de recorrido, python se encarga de saber que quiero recorrer elemento por elemento la cadena, sino que me retornará cada letra como un string aparte

""" funcion para la profundización del try/except
"""
try:
    numero = int(input("Digite un numero")) #usado mas comúnmente para tipificar errores y sus posibles soluciones, tenemos la alternativa del try/except, un condicional que "trata" de realizar una accion, si esta no se realiza, ejecuta una serie de excepciones como respuesta
    print(numero)
except:
    print("Digite un numero por favor!!!")

#   appEnd