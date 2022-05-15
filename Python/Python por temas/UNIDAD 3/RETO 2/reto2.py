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

# De aqui en adelante no se sube a imaster

informacion ={
    'id_cliente': 1,
    'nombre': 'Johana Fernandez', 
    'edad': 3, 
    'primer_ingreso': True
}

print(cliente(informacion))
