""" este archivo esta creado con la finalidad de que puedas extraer partes de código especificas, ejecutarlas,
    modificarlas,etc.
"""

#------------------------ZONA DE CÓDIGO------------------------
datosPersonales = {
    'nombre': 'Carlos', # el elemento de la izquierda es la propiedad a la que le asignamos el valor de la derecha
    'edad': 35,         # todas las propiedades del diccionario van separadas por una coma
    'ciudad': 'Cali',   # pueden listarse propiedades de diferentes tipos en un mismo diccionario
    'teléfono': 3222222,
    'estudiante': True,
    1 : 50,             # las propiedades de un diccionario se pueden listar con diferentes elementos, incluyendo enteros
    2 : "ejemplo"       # estos también pueden albergar elementos de diferentes tipos, como en este caso, un string
}

#-------------------------ZONA DE TEST-------------------------
for i in datosPersonales:      # esta funcion imprime los parametros uno tras otro recorriendo el diccionario, pero no imprime sus valores
    print(i)
print("-------------------------")
for i in datosPersonales:      # esta funcion imprime los valores de estos parametros uno tras otro recorriendo el diccionario
    print(datosPersonales[i])

#appEnd