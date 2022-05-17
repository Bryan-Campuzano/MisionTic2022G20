#   NOTA: los ejercicios propuestos en este pdf se dividen en dos secciones, una, desarrolla meramente y otra seccion en la que
#   se crean las funciones que permiten ejecutar estos algoritmos, para fines de estos apuntes realizaremos
#   directamente las funciones y dentro de ellas los algoritmos con el fin de no interrumpir el proceso de resolución
#   de estos problemas con repeticiones innecesarias

#------------------------ZONA DE CÓDIGO------------------------
""" Diseñar un algoritmo que lea el peso de una persona en libras y devuelva su peso en kilogramo
"""
def pesoLibraAKilo ():
    mns = ""
    cantidadLibras = int(input("Digite el peso en libras: "))
    cantidadKilos = cantidadLibras * 0.453592
    mns = f"el peso equivale a: {cantidadKilos} Kilogramos"
    return mns    


#-------------------------ZONA DE TEST-------------------------
print(pesoLibraAKilo ())
print(pesoLibraAKilo ())
print(pesoLibraAKilo ())



#   appEnd