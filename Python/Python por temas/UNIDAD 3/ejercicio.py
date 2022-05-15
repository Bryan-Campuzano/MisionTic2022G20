hombre = "mas"          # genero hombre
mujer  = "fem" 
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
def totalMujeres (sexoTrabajadores): 
    temp = 0
    for i in sexoTrabajadores:
        if sexoTrabajadores[i] == mujer:
            temp += 1
    return temp

print(totalMujeres(sexoTrabajadores))
