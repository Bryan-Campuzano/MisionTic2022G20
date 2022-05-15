a = True
b = False
print(type(a), type(b))
print(not(a))
#expresiones que arrojan valores booleanos
print(5>8)
print(8>5)
# Sensor puerta--> true: puerta abierta y false: puerta cerrada
# Sensor ventana --> false: ventana abierta y true: ventana cerrada
# hacer un programa que encienda una alarma cuando o la ventana o la puerta 
# o ambas estén abiertas
ventana = True
puerta = False
if puerta or not(ventana):
    print("alarma encendida")
else:
    print("alarma apagada")


