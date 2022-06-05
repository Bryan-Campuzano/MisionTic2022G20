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
import numpy as np      # importa las propiedades de numpy y las asigna a un elemento np

mat = np.array([4,8,2]) # aunque la notación interna del array o 'arreglo' en español es una lista, al imprimir el
print(mat)              # tipo de este elemento, nos regresa 'numpy.ndarray' diciéndonos que es un elemento array 
print(type(mat))
print(mat.shape)        # esta función nos retornas las dimensiones de la matriz al que se le aplica, en este caso nos retorna '(3,)' pues es una matriz de 3 columnas y una fila
print(mat[1])           # retorna el valor de la matriz en la posición 1, empezando la cuenta desde cero, como es de costumbre
mat[1] = 20             # reasigna el valor de la matriz en pa posición 1 a 20
print(mat)              # vemos el cambio de la matriz efectuado
print('---------------separador-------------------')
mat2 = np.array([[5,8,7],[3,5,9]])
print(mat2)
print(type(mat2))
print(mat2.shape)       # retorna las dimensiones de la matriz, en este caso retorna (2,3) primero el numero de filas y después el numero de columnas
print(mat2[0][2])       # retorna el valor de la primera lista en su posición 2, en otras palabras, el valor de la matriz en la posición (1,3)
mat2[0][0] = 1582       # reasigna el valor en la posición (0,0)
print(mat2)             # visualizamos los cambios
print('---------------separador-------------------')
print('\n')             # imprimimos un salto de renglón
mat3 = np.array([[[8,9,5,7],[6,8,4,4],[6,1,2,6]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]]],) # se pueden introducir varias matrices 
print(mat3)
print(mat3.shape)       # nos indica las dimensiones de las matrices almacenadas en el array, estas tienen que ser de las mismas dimensiones para ser almacenadas juntas
mat3[1,2,2]=5000047     # nos retorna '(3, 3, 4)' que indica, cantidad de matrices, filas de estas y columnas de estas en ese orden, la cantidad de matrices se conoce también como 'fondo' o 'profundidad'
print(mat3)             # en este caso el fondo es 3 porque hay tres matrices ordenadas por capas, similar a fichas de domino, o la tercera dimension de un cubo, ejemplo ilustrado en la carpeta 'extras'
print('---------------separador-------------------')
mat4 = np.array([[1,2],[2,3]])
mat5 = np.array([[1,2],[2,3]])
mat6 = mat4 + mat5      # aquí realizamos una suma de matrices, igual que en algebra lineal, la suma de elementos de matrices se realiza por coordenadas o posiciones
print(mat4)             # sumando el valor de la casilla (0,0) de mat 4 con la casilla de coordenadas (0,0) de mat 5, asi, con todos los demás valores de ambas matrices
print(mat5)             # dando como resultado una nueva matriz con las mismas dimensiones de las matrices sumando (tienen que ser de iguales dimensiones para poder ser sumadas) con todos los valores resultados
print(mat6)             # en la misma posición de los sumándos de origen, en este caso la matriz resultado es:
                        #   |2 4|
                        #   |4 6|

#   appEnd