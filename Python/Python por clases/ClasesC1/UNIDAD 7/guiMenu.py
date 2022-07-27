""" construir una Aplicacion que permita cambiar la resolución de la ventana y el color de fondo de la misma
    para el estudio e implementación de los menus normales y de los tipo 'cascada'  
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:                                                           # clase principal de la aplicación
    def __init__(self):                                                     # método constructor de la aplicación
        self.ventana1 = tk.Tk()                                             # ventana principal de la aplicación
        self.menu1 = tk.Menu()                                              # creamos un menu
        self.ventana1.config(menu = self.menu1)                             # creamos la ventana principal y le pasamos el menu como parámetro, para que sea el menu de la ventana principal
        opciones1 = tk.Menu(self.menu1)                                     # agregamos una 'pestaña' o elemento del menu que se llamará opciones
        opciones1.add_command(label = "Rojo",command=self.Rojo)             # agregamos un comando a la pestaña opciones del menu, este comando ejecutara un método a elección, en este caso el método 'Rojo'
        opciones1.add_command(label = "Amarillo",command=self.Amarillo)     # agregamos el comando 'amarillo' este se compone de dos partes, la etiqueta, que es la parte visible en la interfaz
        opciones1.add_command(label = "Azul",command=self.Azul)             # y la otra es el método que se ejecuta al llamarlo, en este caso son métodos que declararemos después
        self.menu1.add_cascade(label='Colores',menu=opciones1)              # añadimos un elemento cascada, que agrupa los elementos que se le asignen en un menu desplegable tipo cascada, recibe una etiqueta identificadora y un menu como parámetro
        opciones2 = tk.Menu(self.menu1)                                     # creamos un segundo sub-menu 
        opciones2.add_cascade(label='640x480',command=self.tamano1)         # creamos una segunda cascada para este submenu, podemos agregar menus de opciones completos o comandos por individual
        opciones2.add_cascade(label='1024x800',command=self.tamano2)        # agregamos un segundo elemento a la cascada, con label y método específicos (con 'métodos específicos o propietarios' me refiero a métodos creados dentro del programa, y no métodos default de alguna clase)
        self.menu1.add_cascade(label='Tamaño', menu=opciones2)              # agregamos el segundo menu al menu principal y le llamamos 'tamaño'
        self.ventana1.mainloop()                                            # loop principal de la aplicación
        
        
    def Rojo(self):                                                         # creamos los métodos propietarios de este programa, en este caso, el método 'Rojo' usa un método de configuración de ventana de tk que permite cambiar el color de fondo de la ventana
        self.ventana1.configure(background='red')
    def Amarillo(self):                                                     # como vemos en el parámetro 'background' hay colores que estan declarados por defecto y que solo con el nombre podemos hacer su implementación
        self.ventana1.configure(background='yellow')
    def Azul(self):
        self.ventana1.configure(background='blue')
    def tamano1(self):                                                      # el método 'tamano1' cambia la variable 'geometry' de la ventana a un tamaño en especifico, solicita un string con una cantidad de pixeles horizontal y vertical separada por una x (como vemos en el método)
        self.ventana1.geometry('640x480')
    def tamano2(self):                                                      # NOTA: no estamos llamando un método, estamos cambiando una variable propia de la ventana creada, eso nos dice que los elementos de las librerías también tienen variables accesibles las cuales podemos acceder y modificar a nuestro antojo
        self.ventana1.geometry('1024x800')
        
#------------------------INICIALIZACIONES---------------------------     
x = Aplicacion()

#   appEnd