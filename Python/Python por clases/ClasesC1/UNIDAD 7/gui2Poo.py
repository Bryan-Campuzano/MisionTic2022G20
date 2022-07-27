""" construimos una ventana con titulo para estudiar el comportamiento de las ventanas y su inicializacion
"""
#------------------------IMPORTACIONES---------------------------

import tkinter as tk    # importamos librería
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:       # creamos la misma ventana que en gui1 pero usando el paradigma de programación orientada a objetos
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.ventana1.mainloop()
       
#------------------------INICIALIZACIONES--------------------------- 
x = Aplicacion()        

#   appEnd
