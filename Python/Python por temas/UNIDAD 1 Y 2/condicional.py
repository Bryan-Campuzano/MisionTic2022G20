#Ralice un progrma que lea un número entero y diga si es mayor o igual a 100.
respuesta = 'S'
while respuesta =='S': #== se utiliza para comparar 
    numero = input("Digite el número: ")
    if int(numero) >= 100:  #casting
        print("El número es mayor o igual a 100")
    else:
        print("El número es menor a 100")
    respuesta = input('Digite "S" para continuar o cualquier tecla para salir')
    
        
 