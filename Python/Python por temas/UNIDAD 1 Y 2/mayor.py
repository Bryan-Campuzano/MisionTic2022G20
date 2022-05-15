# Realice un ejercicio que lea n numeros enteros y nos diga cual
# es el mayor de ellos.   
cantidadNum = int(input("Digite la cantidad de números que va a ingresar:\n"))
final = cantidadNum + 1 
for i in range(1, final):
    numero = int(input(f"ingrese el numero {i}\n")) 
    if i == 1:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
print(f"El mayor de los {cantidadNum} numeros ingresados es {mayor}")    
print(f"El menor de los {cantidadNum} numeros ingresados es {menor}") 
    
    