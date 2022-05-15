#Diseñe un algoritmo para calcular la longitud de la hipotenusa
# (es decir, el lado más largo de un triángulo rectángulo, 
# el opuesto al ángulo recto) utilizando el Teorema de Pitágoras:
# c = √ a2 + b2

def hipotenusa(a,b):
    h = (a**2 + b**2)**0.5
    return h

print(hipotenusa(3,4))