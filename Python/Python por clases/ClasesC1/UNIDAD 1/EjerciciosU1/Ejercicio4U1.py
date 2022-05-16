#   NOTA: la realización de estas soluciones corre por cuenta de un estudiante, si conoces mejores soluciones a este 
#   problema o encuentras algún fallo importante, sientete libre de contactarte conmigo
#   este proceso de aprendizaje lo hacemos entre todos

#------------------------ZONA DE CÓDIGO------------------------
#------------------------CODIGO EN PROCESO------------------------

""" este algoritmo principal busca determinar: 
    
    * Número total de empleado del sexo femenino 
    * Número total de hombres casados que ganan más de 1.000.000 Bs.F. 
    * Número total de mujeres viudas que ganan más de 600.000 Bs. 
    * Edad promedio de los hombres.

en un conjunto de datos relativos de una empresa que abarcan 

    *Edad de la persona 
    
    *Estado civil 
        1. Soltero(a) 
        2. Casado(a) 
        3. Viudo(a) 
    
    *Sexo 
        1. Femenino 
        2. Masculino
    
    *Sueldo
        1. Menos de 600.000 COP 
        2. Entre 600.000 y 1.000.000 COP 
        3. Más de 1.000.000 CO      
"""
#   declaración de variables y constantes

soltero = "sol"         # estado civil soltero
casado  = "cas"         # estado civil casado
viudo   = "vid"         # estado civil viudo

hombre = "mas"          # genero hombre
mujer  = "fem"          # genero mujer

a     = "menosDe600"    # rango salarial de menos de 600.000 COP
b     = "entre100Y1M"   # rango salarial entre 600.000 COP y 1.000.000 COP
c     = "masDe1M"       # rango salarial de mas de 1.000.000 COP

#   listado de las edades de los trabajadores de la empresa
edadesTrabajadores = {
    0 : 21,
    1 : 22,
    2 : 23,
    3 : 24,
    4 : 25,
    5 : 31,
    6 : 32,
    7 : 33,
    8 : 34,
    9 : 35,
    10 :41,
    11 :42,
    12 :43,
    13 :44,
    14 :45,
    15 :51,
    16 :52,
    17 :53,
    18 :54,
    19 :55
}

#   listado de los estados civiles de los trabajadores de la empresa
civilTrabajadores = {
    0 : soltero,
    1 : casado,
    2 : soltero,
    3 : casado,
    4 : soltero,
    5 : casado,
    6 : soltero,
    7 : casado,
    8 : soltero,
    9 : casado,
    10 :casado,
    11 :soltero,
    12 :casado,
    13 :soltero,
    14 :viudo,
    15 :soltero,
    16 :soltero,
    17 :viudo,
    18 :soltero,
    19 :viudo   
}
#   listado del genero de los trabajadores de la empresa
sexoTrabajadores = {
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
#   listado de los rangos salariales de los trabajadores de la empresa
sueldoTrabajadores = {
    "0" : a,
    "1" : a,
    "2" : c,
    "3" : c,
    "4" : b,
    "5" : b,
    "6" : c,
    "7" : a,
    "8" : b,
    "9" : c,
    "10" :a,
    "11" :c,
    "12" :c,
    "13" :a,
    "14" :b,
    "15" :b,
    "16" :a,
    "17" :b,
    "18" :b,
    "19" :b    
}

#   funciones necesarias para la solución
""" esta funcion retorna la cantidad de mujeres que trabajan en la empresa
"""
def totalMujeres (sexoTrabajadores): 
    temp = 0
    for i in sexoTrabajadores:
        if sexoTrabajadores [i] == mujer:
            temp += 1
    return temp

def mayores30 (): 
    temp = 0
    for i in edadesTrabajadores:
        if edadesTrabajadores[i] >= 30:
            temp + 1
    return temp
       
#-------------------------ZONA DE TEST-------------------------
print(totalMujeres(sexoTrabajadores))
print("la cantidad de mujeres en la empresa es: ",mayores30())


#appEnd
