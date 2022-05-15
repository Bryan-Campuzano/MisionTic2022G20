diccionario = {
    'nombre': 'Carlos', 
    'edad': 30,
    'ciudad': 'Cali'
}

print(diccionario)
print(diccionario['edad'])

# Agregando llaves a un diccionario
CantidadEst = {}
print(CantidadEst)
CantidadEst.setdefault('Grado 1', 85)
print(CantidadEst)
CantidadEst.setdefault('Grado 2',65)
print(CantidadEst)
CantidadEst['Grado 3'] = 63
print(CantidadEst)

#Formas de obtener el valor de una llave
print(CantidadEst.get('Grado 1'), CantidadEst.setdefault('Grado 1'), CantidadEst['Grado 1'])

ingresos = dict(nombre='Carlos', edad = 40)
print(ingresos)
# Variable que actúa como un contador: cont = cont + 1 ->> cont +=1
# Variable acumuladora: 
# Acumulador = Acumulador + valor ->> Acumulador += valor