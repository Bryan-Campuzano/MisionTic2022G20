def CDT(usuario:str,capital:int, tiempo:int):
    interes = (capital*0.03*tiempo)/12
    return f"Para  el  usuario  {usuario}  La  cantidad  de  dinero  a  recibir,  según  el  monto  inicial  {capital}  para  un tiempo de {tiempo} meses es: {interes}"

print(CDT('AB1012', 1000000, 3))
    
    
    
