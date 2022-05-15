def saludo():
    print("Hola mundo")
    
saludo()
saludo()
saludo()
saludo()

def suma(num1, num2): #num1 y num2 son los parámetros de la función
    print(num1 + num2)

suma(15,20) #El 15 y el 20 son los argumentos de la función
    
def resta(num1,num2):
    return num1-num2

print(resta(10,8))

def operaciones(a,b,operador):
    if operador == "+":
        return a+b
    elif operador == "-":
        return a-b
    elif operador == "*":
        return a*b
    elif operador == "/":
        return a/b
    else:
        return "Digite un operador válido"
    
def operaciones2(a,b,operador):
    if operador == "+":
        resultado = a+b
    elif operador == "-":
        resultado = a-b
    elif operador == "*":
        resultado= a*b
    elif operador == "/":
        resultado = a/b
    else:
        resultado = "Digite un operador válido"
    return resultado
print("________________________")    
print(operaciones(5,8,"+"))
print(operaciones(5,8,"-"))
print(operaciones(5,8,"*"))
print(operaciones(5,8,"/"))
print(operaciones(5,8,"p"))
print("________________________")
print(operaciones2(5,8,"+"))
print(operaciones2(5,8,"-"))
print(operaciones2(5,8,"*"))
print(operaciones2(5,8,"/"))
print(operaciones2(5,8,"p"))

