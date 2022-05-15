# Los diccionarios se utilizan para almacenar valores en pares
# clave-valor, ejemplo: 'nombre': 'marina'
# Son mutables y no permiten duplicados (claves)

datosPersonales = {
    'nombre': 'Carlos', # llave - valor
    'edad': 35,
    'ciudad': 'Cali',
    'telefono': 3222222,
    'estudiante': True,
    1: 50.5,
    2: 'ejemplo'
}

nombre = 'Juan'
print(nombre)
print(datosPersonales['nombre'])
print(datosPersonales)
print(type(datosPersonales))
print(type(nombre))
print(type(datosPersonales['edad']))
print(type(datosPersonales['estudiante']))
datosPersonales['edad'] = 40 #Los diccionarios son mutables
print(datosPersonales[1])
print('Carlos' in datosPersonales) #devuelve un True si la llave se encuentra en el diccionarios
# métodos
#copy
datosPersonales2 = datosPersonales.copy()
#clear
datosPersonales.clear()
print(datosPersonales)
#pop
datosPersonales2.pop('estudiante')
print(datosPersonales2)

#función len
print(len(datosPersonales2))
del datosPersonales2['edad']
print(datosPersonales2)

for i in datosPersonales2:
    print(i)
    
for i in datosPersonales2:
    print(datosPersonales2[i])
    
#append

