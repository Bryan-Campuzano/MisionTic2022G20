#   NOTA: los ejercicios propuestos en este pdf se dividen en dos secciones, una, desarrolla meramente y otra seccion en la que
#   se crean las funciones que permiten ejecutar estos algoritmos, para fines de estos apuntes realizaremos
#   directamente las funciones y dentro de ellas los algoritmos con el fin de no interrumpir el proceso de resolución
#   de estos problemas con repeticiones innecesarias

#------------------------ZONA DE CÓDIGO------------------------
""" Diseñar un algoritmo que calcule las cuatro operaciones aritméticas básicas
        parametros: a (int): primer cateto del triangulo
                    b (int): segundo cateto del triangulo
                    operador (str): operador que identifica la operacion aritmética a realizar
        retorna:    resultado (double/int): retorna el resulrado de la operacion, siento un entero o un double dependiendo del caso
"""
def operaciones(a,b,operador):   
    if operador == "+":            
         resultado = a+b           
    elif operador == "-":          
         resultado = a-b
    elif operador == "*":
         resultado = a*b
    elif operador == "/":
         resultado = a/b
    else:
        resultado = "Digite un operador valido"
    return resultado

#-------------------------ZONA DE TEST-------------------------
print(operaciones (5,8,"+")) #este es un test de todos los casos de la funcion operaciones
print(operaciones (5,8,"-"))
print(operaciones (5,8,"*"))
print(operaciones (5,8,"/"))
print(operaciones (5,8,"p"))