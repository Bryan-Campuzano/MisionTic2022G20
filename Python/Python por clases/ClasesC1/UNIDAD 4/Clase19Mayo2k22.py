""" continuamos con el tema de contenedores, en esta ocasión vamos a ver diferentes formas de convertir
    estos contenedores en otros, manteniendo y manipulando el contenido a necesidad
"""
""" Conversión de cadena a lista
"""
cadena = 'Colombia'     # elemento en forma de cadena: 'Colombia'
lista = list(cadena)    # elemento en forma de lista: ['C', 'o', 'l', 'o', 'm', 'b', 'i', 'a']
print(lista)            # el resultado es una lista indexada con los elementos de la cadena original separada en cada posición

""" Conversión de lista a cadena
"""
cadena2= ''.join(lista) # el comando join permite concatenar indefinida cantidad de strings y retorna como resultado
print(cadena2)          # una cadena nueva juntando todos los valores en orden. en este caso, agrega todos los valores
                        # de la lista, uno tras otro, en el orden dado por la propia lista

lista2 = [1,5,8,7,3]    # esta lista no se puede concatenar con el comando join pues no son elementos de tipo str

""" Conversión de listas a conjuntos
"""
conjunto = set(lista)   # agrega los elementos de la lista en un conjunto, pero como es un contenedor no indexado
print(conjunto)         # a la hora de solicitar los elementos, se retornaran en un orden aleatorio
                        # ademas de que en un conjunto no se almacenan los elementos repetidos, por lo que si
                        # la cadena contiene caracteres repetidos, se almacenara unicamente uno de ellos

""" Conversion de cadena a diccionario
"""
tempo = list(zip(range(len(cadena)),cadena))        # el comando zip genera una lista de tuplas en las cuales     
print(tempo)                                        # se introducen parejas de (parámetro,valor) con los valores                    
                                                    # en este ejemplo, crea parámetros con los nombres de los Numeros enteros
                                                    # pertenecientes al rango indicado iniciando en cero, y a cada uno de estos Numeros
                                                    # le asigna una letra del string indicado, dando como resultado:
                                                    # [(0, 'C'), (1, 'o'), (2, 'l'), (3, 'o'), (4, 'm'), (5, 'b'), (6, 'i'), (7, 'a')]
                                                    # al introducir la palabra 'Colombia'

diccionario = dict(zip(range(len(cadena)),cadena))  # en este caso podemos crear un diccionario donde sus llaves son
print(diccionario)                                  # los valores enteros dados por la función zip y sus valores son
                                                    # las letras de la cadena introducida, al introducir el string 'Colombia'
                                                    # da como resultado: {0: 'C', 1: 'o', 2: 'l', 3: 'o', 4: 'm', 5: 'b', 6: 'i', 7: 'a'}

""" Conversión desde diccionarios
"""
print(diccionario.keys())               # retorna los parámetros de cada elemento del diccionario pero no sus valores
print(diccionario.values())             # retorna el valor de cada uno de los parámetros del diccionario, pero sin su llave
print(diccionario.items())              # retorna los parámetros y sus valores en tuplas
cadena3 = ''.join(diccionario.values()) # crea una cadena con los valores de los elementos guardados en los parámetros del diccionario
                                        # es una forma de transformar diccionarios en cadenas
print(cadena3)

#   NOTA: para mas material de conversiones, consultar el pdf 'ConversionColecciones' en la carpeta de 'Extras' o el la unidad 4 de 
#   'python por temas' allí se encuentras mas métodos de transformación y manipulación de elementos en python, pero los vistos aquí 
#   son los mas importantes o menos intuitivos el resto de transformaciones son variaciones de las vistas aquí

""" introducción a la función lambda
        lambda es una función anónima o privada, esto quiere decir que es una función que solo tiene sentido
        o funciona en determinada clase o algoritmo
        lambda sirve para declarar funciones simples dentro de un algoritmo, aquellas que se puedan definir en una
        sola linea, ayuda a reducir el tamaño del codigo
        la notación de lambda es:
        lambda 'parámetros': cuerpo de la función
""" 
cuadrado = lambda a: a**2   # la función 'cuadrado' recibe como parámetro 'a' y la eleva al cuadrado, retorna el resultado
print(cuadrado(5))          # 25
print(cuadrado(10))         # 100
print(cuadrado(6))          # 36

def operaciones(a,b, fn):   # la función operaciones recibe como parámetro dos valores y una función anónima
    return fn(a,b)          # retorna la función evaluada en los parámetros de entrada

suma = operaciones(10,9, lambda x, y: x+y)  # declaro un valor 'suma' el cual es el resultado de la operación 'lambda' de suma
print(suma)
resta = operaciones(10,9, lambda x, y: x-y) # puedo variar el cuerpo de lambda para hacer las funciones necesarias 
print(resta)

""" argumentos en python
        *args se usa para declarar que la cantidad de parámetros introducidos a la función es variable 
        **kwargs se usa para declarar una cantidad de parámetros variable que, ademas esta indexado   
"""
def suma(*args):    # args es una tupla de parámetros, en vez de pasar a la función parámetros 'a' 'b' etc, se le pasa una cantidad variable de parámetros a operar
    total = 0       # 'args' es solo una convención, el parámetro variable puede llamarse 'elementos' lo que declara que es una cantidad de parámetros variable no indexada es el '*'
    for i in args:  # como es una tupla, es susceptible a recorridos
        total +=i
    return total

print(suma(8,9,9,7,6,5))

def suma2(**kwargs):        # Kwargs es un diccionario de parámetros, pero en esta ocasión son parámetros indexados, quiere decir que cada parámetro tiene una llave que le identifica
    total =0                # la declaración de los elementos variables indexados, se hace con '**'
    for i in kwargs:
        total +=kwargs[i]   # los diccionarios también son susceptibles a recorridos, pero se solicitan los valores de los parámetros
    return total  
print(suma2(a=3,b=14,c=79))

""" introducción a las matrices
        las matrices son cuadriculas de valores, traídas de las matemáticas convencionales, para la manipulación de funciones lineales
        en grandes cantidades. su principal uso es de manipulación, lectura y almacenamiento de datos relacionados. si poseemos, por ejemplo,
        dos tuplas de la forma (a,b) y (c,d) podemos organizar estas parejas en otro contenedor de forma [(a,b),(c,d)]
        al formar matriz tendríamos un elemento similar a
        
        |a b|
        |c d|
        
        cada uno de estas posiciones tiene coordenadas de posición, con las cuales se puede recorrer la matriz y extraer el valor de parámetro
        por ejemplo, el valor 'a' se encuentra en la posición (1,1) en otras palabras, el valor a esta 'ubicado en el primer valor de la primera tupla'

        encuentras un ejemplo ilustrado en el elemento 'matriz.jpg' en la sección de 'Extras' y en la unidad 4 de 'python por temas' 
    
    para la creación, manipulación y demás operaciones dentro de las matrices vamos a importar la librería numpy
    las librerías son colecciones enteras de codigo, con funciones, test y documentación, que podemos usar en nuestros proyectos
"""



#   appEnd