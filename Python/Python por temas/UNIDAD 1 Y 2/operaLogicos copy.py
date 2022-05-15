#Realizar un programa que indique si una persona debe presentar 
#la declacion de renta. Las condiciones para presentar este impuesto son:
#Ser mayor de edad y
#Tener ingresos anuales superiores o iguales a $50.831.000
#and    F   F   F
#and    F   V   F
#and    V   F   F
#and    V   v   V

#or    F   F   F
#or    F   V   V
#or    V   F   V
#or    V   v   V
    
edad = int(input("Digite su edad: "))
ingresos = int(input("¿Cuáles son sus ingresos mensuales?"))
ingresoAnual = ingresos * 12
if edad < 18 or ingresoAnual < 50831000:
    print("Usted no debe presentar la declaración de renta")
else:
    print("Usted debe presentar declaración de renta")