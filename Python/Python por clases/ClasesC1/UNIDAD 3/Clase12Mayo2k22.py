""" continuación de la explicación de diccionarios python
"""
#   agregando llaves a diccionarios
CantidadEst={}                          # crea un diccionario vació
print(CantidadEst)                      # retorna una llave vacía
CantidadEst.setdefault('Grado 1', 85)   # agrega al diccionario un parámetro llamado "grado 1" y tiene 85 estudiantes
print(CantidadEst)                      # retorna un diccionario con un elemento
CantidadEst.setdefault('Grado 2',65)    # agrega al diccionario un parámetro llamado "grado 2" y tiene 65 estudiantes
print(CantidadEst)                      # retorna un diccionario con dos elemento
CantidadEst['Grado 3']=63               # agrega al diccionario un parámetro llamado "grado 3" y tiene 63 estudiantes
print (CantidadEst)                     # retorna un diccionario con tres elemento

"""Formas de obtener el valor de una llave
"""
print(CantidadEst.get('Grado 1'), CantidadEst.setdefault('Grado 1'),CantidadEst['Grado 1'])

"""bosquejo solución del reto 2
"""
def cliente(informacion:dict)->dict:
    
    if informacion['edad'] > 18:
        atraccionV = 'X-Treme'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            pass #calculo de la boleta con descuento
        else:
            pass #aplico el valor pleno de la boleta
    elif informacion['edad']>=15 and informacion['edad']<=18:
        atraccionV = 'Carros chocones'
        aptoV = True
    elif informacion['edad']>=7 and informacion['edad']<15:
        atraccionV = 'Sillas voladoras'
        aptoV = True
    else:
        atraccionV = 'N/A'
        aptoV = False
        total_boletaV = 'N/A'
    
    nuevoDiccionario ={
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion': atraccionV,
        'apto':aptoV,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta': 'En construcción'
    }
    return nuevoDiccionario

# De aquí en adelante no se sube a imaster

informacion ={
    'id_cliente': 1,
    'nombre': 'Johanna Fernandez', 
    'edad': 3, 
    'primer_ingreso': True
}

print(cliente(informacion))

""" solución al problema de recorrido de diccionario de Bryan
"""
hombre = "mas"          # genero masculino
mujer  = "fem"          # genero femenino
sexoTrabajadores = {    # registro de genero de los 20 empleados de la empresa
    "0" : mujer,
    "1" : mujer,
    "2" : mujer,
    "3" : hombre,
    "4" : mujer,
    "5" : mujer,
    "6" : hombre,
    "7" : hombre,
    "8" : mujer,
    "9" : mujer,
    "10" :mujer,
    "11" :hombre,
    "12" :hombre,
    "13" :mujer,
    "14" :hombre,
    "15" :hombre,
    "16" :mujer,
    "17" :mujer,
    "18" :mujer,
    "19" :hombre   
} 
def totalMujeres (sexoTrabajadores):        # NOTA: el error en el codigo original era que, para que esta función de recorrido 
    temp = 0                                # funcione, se debía pasar el diccionario a recorrer como parámetro de entrada, esto para saber a que 
    for i in sexoTrabajadores:              # diccionario tiene que aplicarse el recorrido
        if sexoTrabajadores[i] == mujer:
            temp += 1
    return temp

print(totalMujeres(sexoTrabajadores))       # al momento de la función necesitar un parámetro de entrada, es necesario introducir el diccionario como
                                            # sexoTrabajadores como parámetro al momento de llamar a la función
""" introducción a las listas
"""
MarcasCarros = ['Audi','Chevrolet','Renault','Toyota']  # a diferencia de los diccionarios, la notación de las listas se hace con "[]" en vez de corchetes
datosPersonales = ['Carlos', 40, True]                  # no hay que guardar sus elementos dentro de keys o parámetros, solo se guardan los valores a usar
print(MarcasCarros)                                     # puede contener valores de diferentes tipos, cadenas, enteros etc
print(datosPersonales)

frutas = list(('manzana','pera','fresa'))               # contienen posiciones especificas para cada elemento
print(frutas)
frutas[2]='piña'                                        # reemplaza el elemento en la posición 2, iniciando el conteo desde cero
print(frutas)

for i in frutas:
    print(i)
    
#   appEnd