#   NOTA: la realización de estas soluciones corre por cuenta de un estudiante, si conoces mejores soluciones a este 
#   problema o encuentras algún fallo importante, sientete libre de contactarte conmigo
#   este proceso de aprendizaje lo hacemos entre todos

#------------------------ZONA DE CÓDIGO------------------------

#   EJERCICIO 3 PROBLEMA A
""" Funcion que calcula la superficie de un triangulo 
"""
def areaTriangulo(b,h):
    areaA = (h * b) / 2
    return areaA
#   EJERCICIO 3 PROBLEMA B
""" Funcion que calcula el area de un circulo
"""
import numpy #importa la clase numpy para usar el valor de pi que esta definida en esta
def areaCirculo(radioB):
    areaB = (radioB ** 2) * numpy.pi
    return areaB

#   EJERCICIO 3 PROBLEMA C
""" Funcion que calcula la base de un triángulo, teniendo la superficie y la altura
"""
def baseTriangulo (areaC,h):
    baseC = (areaC * 2) / h
    return baseC

#   EJERCICIO 3 PROBLEMA D  
""" Funcion que calcula el radio de un círculo, teniendo el área
"""
def radioCirculo (areaD):
    radioD = (areaD/numpy.pi) ** (1/2)
    return radioD
   
#-------------------------ZONA DE TEST-------------------------
#PROBLEMA A
print("-----------A--------------")
print(areaTriangulo(3,5))       #7.5
print(areaTriangulo(5,7))       #17.5
print(areaTriangulo(7,9))       #31.5
print(areaTriangulo(9,11))      #49.5 

#PROBLEMA B
print("-----------B--------------")
print(baseTriangulo(areaTriangulo(3,5),5))      #3.0
print(baseTriangulo(areaTriangulo(5,7),7))      #5.0
print(baseTriangulo(areaTriangulo(7,9),9))      #7.0
print(baseTriangulo(areaTriangulo(9,11),11))    #9.0

#PROBLEMA C
print("-----------C--------------")
print(areaCirculo(5))   #78.53981633974483
print(areaCirculo(6))   #113.09733552923255
print(areaCirculo(7))   #153.93804002589985
print(areaCirculo(8))   #201.06192982974676
#PROBLEMA D
print("-----------D--------------")
print(radioCirculo(areaCirculo(5))) #5.0
print(radioCirculo(areaCirculo(6))) #6.0
print(radioCirculo(areaCirculo(7))) #7.0
print(radioCirculo(areaCirculo(8))) #8.0

#appEnd