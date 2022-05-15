
#   NOTA: la realización de estas soluciones corre por cuenta de un estudiante, si conoces mejores soluciones a este 
#   problema o encuentras algún fallo importante, sientete libre de contactarte conmigo
#   este proceso de aprendizaje lo hacemos entre todos

#------------------------ZONA DE CÓDIGO------------------------

""" Funcion que recibe 4 números y determina cual es el mayor de estos 
"""
def numMayor(n1 : int,n2 : int,n3 : int,n4 : int): 
    numeroMayor = 0
    listaNumeros = {
        0 : n1,
        1 : n2,
        2 : n3,
        3 : n4
    }
    for i in listaNumeros:
        if listaNumeros[i] > numeroMayor:
            numeroMayor = listaNumeros[i]
        else:
            numeroMayor = numeroMayor
    return  numeroMayor 
    

#-------------------------ZONA DE TEST-------------------------

print(numMayor(1,2,3,4))
print("---------------")
print(numMayor(7,4,3,4))
print("---------------")
print(numMayor(5,10,15,20))
print("---------------")
print(numMayor(1,1,1,1))
print("---------------")

#appEnd

    
        
    