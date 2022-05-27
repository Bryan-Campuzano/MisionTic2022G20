#   NOTA: la realización de estas soluciones corre por cuenta de un estudiante, si conoces mejores soluciones a este 
#   problema o encuentras algún fallo importante, siéntete libre de contactarte conmigo
#   este proceso de aprendizaje lo hacemos entre todos

#------------------------ZONA DE CÓDIGO------------------------

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
trabajadores = {
    0:[21,soltero,mujer ,a],
    1:[22,casado ,mujer ,a],
    2:[23,soltero,mujer ,c],
    3:[24,casado ,hombre,c],
    4:[25,soltero,mujer ,b],
    5:[31,casado ,mujer ,b],
    6:[32,soltero,hombre,c],
    7:[33,casado ,hombre,a],
    8:[34,soltero,mujer ,b],
    9:[35,casado ,mujer ,c],
    10:[41,casado ,mujer ,a],
    11:[42,soltero,hombre,c],
    12:[43,casado ,hombre,c],
    13:[44,soltero,mujer ,a],
    14:[45,viudo  ,hombre,b],
    15:[51,soltero,hombre,b],
    16:[52,soltero,mujer ,a],
    17:[53,viudo  ,mujer ,b],
    18:[54,soltero,mujer ,b],
    19:[55,viudo  ,hombre,b]
}
#   funciones necesarias para la solución
""" esta función retorna la cantidad de mujeres que trabajan en la empresa
"""
def totalMujeres (trabajadores): 
    temp = 0
    temp2 = "no hay empleados con estas características"
    for i in trabajadores:
        if trabajadores [i][2] == mujer:
            temp += 1
            temp2 = f"el total de mujeres en la empresa es de: {temp}"
    return temp2

""" esta función retorna la cantidad de hombres, casados y que ganan mas de 1.000.000 COP que trabajan en la empresa
"""
def totalHombresCasadosC (trabajadores): 
    temp = 0
    temp2 = "no hay empleados con estas características"
    for i in trabajadores:
        if trabajadores [i][2] == hombre and trabajadores [i][1] == casado and trabajadores [i][3] == c:
            temp += 1
            temp2 = f"el numero total de hombres casados que ganan mas de 1.000.000 COP mensual es de: {temp}"
    return temp2

""" esta función retorna la cantidad de mujeres, viudas y que ganan ,mas de 600.000 COP que trabajan en la empresa
"""
def totalMujeresViudasByC (trabajadores): 
    temp = 0
    temp2 = "no hay empleados con estas características"
    for i in trabajadores:
        if trabajadores [i][2] == mujer and trabajadores [i][1] == viudo and trabajadores [i][3] != a:
            temp += 1
            temp2 = f"el numero total de mujeres viudas que ganan mas de 600.000 COP mensual es de: {temp}"
    return temp2

""" esta función retorna la edad promedio de los trabajadores hombres de la fabrica
"""     
def promedioEdadHombres (trabajadores): 
    temp0 = 0
    temp1 = 0
    prom  = 0.0
    temp2 = "no hay empleados con estas características"
    for i in trabajadores:
        if trabajadores [i][2] == hombre :
            temp0 += 1
            temp1 += trabajadores [i][0]
            prom = temp1/temp0
            temp2 = f"la edad promedio de los hombres de la fabrica es de: {prom}"
    return temp2

#-------------------------ZONA DE TEST-------------------------
print(totalMujeres(trabajadores))
print(totalHombresCasadosC(trabajadores))
print(totalMujeresViudasByC(trabajadores))
print(promedioEdadHombres(trabajadores))

#   appEnd
