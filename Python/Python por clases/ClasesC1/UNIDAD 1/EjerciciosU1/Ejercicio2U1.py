#   NOTA: la realización de estas soluciones corre por cuenta de un estudiante, si conoces mejores soluciones a este 
#   problema o encuentras algún fallo importante, siéntete libre de contactarte conmigo
#   este proceso de aprendizaje lo hacemos entre todos

#------------------------ZONA DE CÓDIGO------------------------

""" Función que recibe un numero determina si este es primo o no
"""
def esPrimo(num):
    estado = True
    mensaje = ""
    divisor = 0
    for i in range(2,num):
        if num % i == 0:
            if i == num:
                estado = True
            else:
                estado = False
                divisor = i
    if estado == True:
        mensaje = "el numero SI es primo"
    else:
        mensaje = "el numero NO es primo ",divisor," es divisor"
    return mensaje          
    
#-------------------------ZONA DE TEST-------------------------

print (esPrimo(13))     # el numero SI es primo
print (esPrimo(14))     # el numero No es primo 2 es divisor
print (esPrimo(887))    # el numero SI es primo
print (esPrimo(333))    # el numero No es primo 3 es divisor
print (esPrimo(1001))   # el numero No es primo 7 es divisor

#appEnd