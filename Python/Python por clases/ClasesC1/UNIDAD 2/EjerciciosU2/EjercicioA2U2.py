#   NOTA: los ejercicios propuestos en este pdf se dividen en dos secciones, una, desarrolla meramente y otra seccion en la que
#   se crean las funciones que permiten ejecutar estos algoritmos, para fines de estos apuntes realizaremos
#   directamente las funciones y dentro de ellas los algoritmos con el fin de no interrumpir el proceso de resolución
#   de estos problemas con repeticiones innecesarias

#------------------------ZONA DE CÓDIGO------------------------
""" Diseñar un algoritmo que calcule la hipotenusa de un triangulo
        parametros: a (int): primer cateto del triangulo
                    b (int): segundo cateto del triangulo
        retorna:    mns (string): cadena de caracteres de la forma 'el valor de la hipotenusa del triangulo es: c (double) '
"""
def calculadoraHipotenusa (a,b):
    mns = ""
    c = ((a ** 2)+(b ** 2)) ** (1/2)
    mns = f"el valor de la hipotenusa del triangulo es: {c}"
    return mns    

#-------------------------ZONA DE TEST-------------------------
print(calculadoraHipotenusa (3,4))
print(calculadoraHipotenusa (4,6))
print(calculadoraHipotenusa (5,6))



#   appEnd