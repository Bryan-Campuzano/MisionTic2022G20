""" en esta clase se nos introduce el concepto de programación orientada a objetos 'POO'
    el cual es un paradigma de programación usado en varios lenguajes por la facilidad a la hora de entender el
    codigo por el programador. consiste en crear 'objetos' entendidos como partes de codigo a las cuales se le asocian adjetivos
    métodos e informacion especifica, por ejemplo, si en nuestro codigo vamos a manejar la informacion de un cliente, podemos crear
    'cliente' como un objeto el cual tiene propiedades (parámetros) tiene acciones que ejecuta (métodos o funciones) y tiene relación 
    con otros objetos. para el manejo de los objetos creamos lo que se llama en programación como
    'Clase'. las clases representan conceptos o ideas, en programación se suele decir que los objetos son 'instancias' de las clases, por ejemplo,
    si tengo una clase llamada 'perro' esta va a tener parámetros como 'raza''nombre''edad''peso' etc, y un objeto o instancia de esta clase sería 
    un perro en concreto, con informacion especifica ('pitbull''Zeus''2''30 KG'etc)
    pueden haber clases que engloben instancias de otras clases, como por ejemplo la clase que se encarga del entorno gráfico, el cual necesita
    de otras clases para su funcionamiento, estas son llamadas relaciones. 
"""
class Persona:
    def crear(self, nombre:str,apellido:str):   # todas las clases, por lo general tiene un método básico llamado método 'constructor' el cual es el
        self.nombre = nombre                    # encargado de crear el objeto con los parámetros necesarios establecidos en la clase
        self.apellido =apellido                 # la clase persona se establece con dos parámetros (nombre y apellido) y dos métodos (crear y mostrar)
                                                # el parámetro 'self' hace referencia a una instancia temporal a la cual se le asignan las variables de construcción de objeto
    def mostrar(self):                          # en español seria como decir 'esta persona tendrá un nombre y un apellido y su informacion se podrá crear e imprimir' al momento 
        print(self.nombre, self.apellido)       # de construir el objeto, asignara la informacion a las variables PROPIAS de la clase, se suele usar 'self' por convención aunque puede ser otra palabra similar 
                                                # siempre y cuando sea el primer parámetro de la clase creada

x = Persona()                                   # se realizó una instancia a la clase persona (x es una persona)
print(type(x))
                                                # x.mostrar(), no se puede utilizar antes de "crear" pues en este momento el objeto no existe
x.crear('Camilo','Arce')                        # la instancia pasa a ser un objeto (persona llamada Camilo Arce)
x.mostrar()                                     # este método creado dentro de persona imprime la informacion del objeto en cuestión

class Estudiante:                               # por convención o buena praxis del programador, las clases se crean con la primera letra en mayúscula
    def __init__(self,nombre:str,apellido:str): # el método init, al igual que el método 'crear' de la clase 'Persona' es un método constructor, pero con la particularidad de que se ejecuta al momento de crear el objeto
        self.nombre = nombre
        self.apellido = apellido
        self.nota = float(input('Digite la nota del estudiante:\n'))    # no toda la informacion dela clase tiene que establecerse como parámetro
    def imprimir(self):                                                 # en este caso 'nota' hace parte de la informacion de la clase 'Estudiante' pero se solicita como input
        print(self.nombre, self.apellido, self.nota)
    def aprobar(self):
        print('Aprobó') if self.nota >= 3.0 else print('No aprobó')     # cada vez el codigo se hace mas condensado, en cada paso que damos hay que tener en cuenta y tomarse 
                                                                        # el tiempo de procesar bien las lineas de codigo para entender su funcionamiento
        
y = Estudiante('Juan','Pinto')  # como el método 'init' se ejecuta al mismo tiempo que se crea el objeto, es necesario pasar la informacion necesaria como parámetro 
y.nombre='Pedro'
y.imprimir()
y.aprobar() 

""" Implemente una clase llamada operaciones, en la cual se cargan dos números decimales en el método __init__ y debe tener 4 métodos para realizar 
    suma, resta, multiplicación y división
"""
class Operaciones:
    def __init__(self,x:float,y:float):
        self.x = x  
        self.y = y
    def sum(self):
        print(f'La suma es: {self.x + self.y}')
    def sub(self):
        print(f'La resta es: {self.x - self.y}')
    def mul(self):
        print(f'La multiplicación es: {self.x * self.y}')
    def div(self):
        try:
            print(f'La división es: {self.x / self.y}') # aquí tenemos en cuenta valores de division indeterminados
        except:
            print(f'División no válida')
            
x = Operaciones(55.40,35.9)     
x.sum()
x.sub()
x.mul()
x.div() 

""" la herencia es un tipo de relación entre clases, la cual define una jerarquía entre clases, estableciendo clases de mayor rango que otras,
    cuando una clase hereda las propiedades de otra, se dice que esta clase es de un orden inferior 
"""
# Clase superior o 'Madre'
class Persona: 
    def __init__(self, nombre:str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido
    def imprimir(self):
        print(self.nombre, self.apellido)
        
x = Persona('Juan','Pinto')
x.imprimir()

# Clase inferior o 'hija'
class Estudiante(Persona):  # la herencia se establece cuando esta clase solicita métodos y parámetros mediante la importación de una clase de orden superior 
    def saludo(self):       # en este caso la jerarquía es bastante clara, todos los estudiantes son personas pero no todas las personas son estudiantes, esto permite la posible creación de otra clase
        print(f'Bienvenido {self.nombre}')

y = Estudiante('María','Rincón')
y.imprimir()
y.saludo()
print(type(x),type(y))

""" aquí comenzamos con el tema de interfaces gráficas, iniciando con esto la unidad numero 7, hasta este punto del curso, hemos introducido, manipulado y creado
    relaciones entre clases y objetos mediante la terminal de VSC (o editor de texto usado) mediante comandos como 'print' o 'input'
    pero cuando desarrollamos software con el usuario final en mente, no podemos asumir que el codigo sera ejecutado en un programa con un compilador
    que permita la interacción que nos da la terminal (esta es mayormente usada para detectar problemas y corroborar el funcionamiento pero no para un usuario final)
    es por esto que necesitamos una forma en la que el usuario pueda interactuar con el programa. como los elementos gráficos son bastante específicos 
    manejaremos los archivos en documentos separados de python. indicaremos la fecha de realización de cada elemento gráfico para su correcto seguimiento.  
"""

#   appEnd