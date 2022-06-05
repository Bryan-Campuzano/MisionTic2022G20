""" realización del esqueleto del reto 3

    ACLARACIÓN: esta parte del codigo no sera compartido por motivos de posibles inconvenientes de copia y plagio
    si desea ver el contenido de este esquema lo puede consultar el los repositorios github de maestros habilitados
    una vez termine el plazo de entrega de este reto se compartirá el esquema de solución mas no la solución integral
"""

""" continuación con el tema de numpy y las matrices
"""
import numpy as np

matriz = np.zeros((2,3))            # crear matriz de solo ceros con las dimensiones dadas 
print(matriz)
print(type(matriz[1,1]))            # esto nos retorna el tipo de dato, en este caso nos retorna 'numpy.float64' o Numeros de coma flotante en base de 64 bit, aunque para el desarrollo de este curso de momento no es relevante, pr lo menos ahora
matriz2 = np.ones((4,3))            # crear matriz de solo unos
print(matriz2)
matriz3 = np.full((3,3),True)       # crea una matriz con el valor de 'true' en todas sus posiciones
print(matriz3)
matriz4 = np.eye(5)                 # matriz identidad, la matriz identidad se puede entender como el elemento neutro de las multiplicaciones de matrices (como lo es el 1 en la multiplicación ordinaria) su uso se da normalmente en algebra lineal
print(matriz4)
matriz5 = np.random.random((4,4))   # crea una matriz con Numeros 'aleatorios' en este caso, por defecto numpy nos ofrece Numeros aleatorios entre 0 y 1 
print(matriz5)                      
matriz6 = np.full((4,4),10)         # matriz de 4x4 con el valor 10 en todas sus posiciones
print(matriz6)
matriz7 = matriz5 * matriz6         # esta operación hace una multiplicación directa entre los elementos que comparten coordenadas de las dos matrices
print(matriz7)

#   appEnd