#Herencia es una relación entre clases
#Se puede definir una clase de la clase que herede propiedade y método de otra clase
#Clase padre(clase principal o clase base), esta es la clase de la que se hereda
#Clase hija(clase secundaria o clase derivada), esta es la clase que hereda

class Persona: # Clase Padre
    def __init__(self, nombre:str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido
    def imprimir(self):
        print(self.nombre, self.apellido)
        
x = Persona('Juan','Pinto')
x.imprimir()

# Clase hija
class Estudiante(Persona):
    def saludo(self):
        print(f'Bienvenido {self.nombre}')

y = Estudiante('María','Rincón')
y.imprimir()
y.saludo()
print(type(x),type(y))

        
        
        