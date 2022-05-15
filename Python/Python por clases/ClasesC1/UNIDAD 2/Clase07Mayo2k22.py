""" introducción a los diccionarios de Python
""" 
#   los diccionarios guardan valores en pares, conocidas como clave : valor
#   ejemplo: "nombre":"Bryan"
#   son mutables y no permiten duplicados, puedo cambiar su información pero no tener mas de un elemento idénticos en toda su extencion

""" declaración de un diccionario con información básica y varios de sus metodos
"""
datosPersonales = {
    'nombre': 'Carlos', # el elemento de la izquierda es la propiedad a la que le asignamos el valor de la derecha
    'edad': 35,         # todas las propiedades del diccionario van separadas por una coma
    'ciudad': 'Cali',   # pueden listarse propiedades de diferentes tipos en un mismo diccionario
    'teléfono': 3222222,
    'estudiante': True,
    1 : 50,             # las propiedades de un diccionario se pueden listar con diferentes elementos, incluyendo enteros
    2 : "ejemplo"       # estos también pueden albergar elementos de diferentes tipos, como en este caso, un string
}

print(datosPersonales['nombre'])   # uno puede solicitar una o varias propiedades del diccionario
print(datosPersonales)             # esto imprime una concatenacion de todas las propiedades del diccionario
print(type(datosPersonales))       # esto nos retorna un resultado que dice <class dict> que indica que es un elemento de clase diccionario
datosPersonales['edad'] = 40       # las propiedades de los diccionarios son mutables y se puede cambiar su valor, incluso se puede cambiar el tipo de dato almacenado en estos
print('Carlos' in datosPersonales) # en este print el 'in' es un carácter comparativo, retorna un true si esta propiedad existe, false de lo contrario. NOTA: busca la propiedad mas no busca los valores de esta
                                   # en este caso retornaria false, porque 'carlos' no es una propiedad, es un valor guardado dentro de la propiedad llamada 'nombre'
print("-------------------------------------------")
#   introducción a metodos
#   los metodos son funciones especificas de una clase, hacen procesos específicos similares a las funciones
#   estas funciones son especificas de cada clase, aunque hay algunos metodos que se usan en diferentes tipos de datos

datosPersonales2 = datosPersonales.copy()   # esta funcion copia toda la información de un diccionario y, como en este caso, la asigna a otro diccionario
datosPersonales.clear()                     # esta funcion deja vació el diccionario en su totalidad, tanto los parametros como sus valores  
#print(datosPersonales)
datosPersonales2.pop('estudiante')          # esta funcion elimina algún parametro en concreto, conservando asi el resto de parametros y valores
print(datosPersonales2) 
len(datosPersonales2)                       # esta funcion me indica la cantidad de parametros de un diccionarios, dicho de otra forna, retorna el tamaño del diccionario entendido como la cantidad de sus parametro.setdefault()

print ("------------------------------------------")

for i in datosPersonales2:      # esta funcion imprime los parametros uno tras otro recorriendo el diccionario, pero no imprime sus valores
    print(i)

for i in datosPersonales2:      # esta funcion imprime los valores de estos parametros uno tras otro recorriendo el diccionario
    print(datosPersonales2[i])

#   appEnd