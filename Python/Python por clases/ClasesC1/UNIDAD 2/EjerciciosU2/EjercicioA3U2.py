#   NOTA: los ejercicios propuestos en este pdf se dividen en dos secciones, una, desarrolla meramente y otra seccion en la que
#   se crean las funciones que permiten ejecutar estos algoritmos, para fines de estos apuntes realizaremos
#   directamente las funciones y dentro de ellas los algoritmos con el fin de no interrumpir el proceso de resolución
#   de estos problemas con repeticiones innecesarias

#------------------------ZONA DE CÓDIGO------------------------
""" Diseñar un algoritmo que lea una distancia en millas a kilometros y de kilometros a millas
"""
def distanciaMillaYKilometro ():
    mns = ""
    d = 0
    distancia = int(input("Digite la distancia: "))
    unidades = str(input("Digite las unidades (millas o kilometros)"))
    if unidades == "millas":
        d = distancia * 1.60934
        mns = f"la distancia en millas equivale a: {d} Kilometros"
    elif unidades == "kilometros":
        d = distancia * 0.621371
        mns = f"la distancia en kilometros equivale a: {d} millas"
    else: 
        mns = "introduzca unidades validas"
    return mns    

#-------------------------ZONA DE TEST-------------------------
print(distanciaMillaYKilometro ())
print(distanciaMillaYKilometro ())
print(distanciaMillaYKilometro ())

#   appEnd