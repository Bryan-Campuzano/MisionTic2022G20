#Realizar un programa que indique si una persona debe presentar 
#la declacion de renta. Las condiciones para presentar este impuesto son:
#Ser mayor de edad y
#Tener ingresos anuales superiores o iguales a $50.831.000
edad = int(input("Digite su edad: "))
ingresos = int(input("¿Cuáles son sus ingresos mensuales?"))
ingresoAnual = ingresos * 12
if edad > 17 and ingresoAnual >= 50831000:
    print("Usted debe presentar la declaración de renta")
else:
    print("Usted no debe presentar declaración de renta")