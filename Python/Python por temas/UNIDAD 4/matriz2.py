import numpy as np

# crear matriz de solo ceros
matriz = np.zeros((2,3))
print(matriz)
print(type(matriz[1,1]))
# crear matriz de solo unos
matriz2 = np.ones((4,3))
print(matriz2)
matriz3 = np.full((3,3),True)
print(matriz3)
matriz4 = np.eye(5) #matriz identidad
print(matriz4)
matriz5 = np.random.random((4,4))
print(matriz5)
matriz6 = np.full((4,4),10)
matriz7 = matriz5 * matriz6
print(matriz7)