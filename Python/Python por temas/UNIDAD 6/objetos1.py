#Programación orientada a objetos Poo
#Python es un lenguaje oreintado a objetos
#Casi todo en python es un objeto
#Clase, es un modelo o patrón del cual se pueden crear múltiples objetos
#Cuando se crea una clase, se definen propiedades o atributos y métodos o funciones
#Hay que crear la clase, para poder crear los objetos
#Cuano creamos un objeto, es lo mismo que decir crear una INSTANCIA de la clase 
from sklearn.feature_selection import SelectFdr


class Persona:
    def crear(self, nombre:str,apellido:str):
        self.nombre = nombre 
        self.apellido =apellido
        
    def mostrar(self):
        print(self.nombre, self.apellido)
    
x = Persona() # se realizó una instancia a la clase persona
print(type(x))
#x.mostrar(), no se puede utilizar antes de "crear"
x.crear('Camilo','Arce')
x.mostrar()

#método constructor, es un metodo que se ejecuta automáticamente cuando el
#objeto es creado
#En Python, ese método se llama __init__    
#El método __init__ es un método especial, su principal objetivo es inicializar
#los atributos o propiedades de un objeto
#Este método no retorna datos y recibe parámetros para inicializar los atributos

class Estudiante:
    def __init__(self,nombre:str,apellido:str):
        self.nombre = nombre
        self.apellido =apellido
        self.nota = float(input('Digite la nota del estudiante:\n'))
    def imprimir(self):
        print(self.nombre, self.apellido, self.nota)
    def aprobar(self):
        print('Aprobó') if self.nota >= 3.0 else print('No aprobó')
        
y = Estudiante('Juan','Pinto')
y.nombre='Pedro'
y.imprimir()
y.aprobar()        
        
        
    
        
    




    