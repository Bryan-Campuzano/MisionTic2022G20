""" este archivo esta creado con la finalidad de que puedas extraer partes de código especificas, ejecutarlas,
    modificarlas,etc.
"""
import numpy as np

#------------------------ZONA DE CÓDIGO------------------------
mat3 = np.array([[[8,9,5,7],[6,8,4,4],[6,1,2,6]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]]],) # se pueden introducir varias matrices 
print(mat3)
print(mat3.shape)       # nos indica las dimenciones
mat3[1,2,2]=5000047
print(mat3)



#-------------------------ZONA DE TEST-------------------------

#   appEnd