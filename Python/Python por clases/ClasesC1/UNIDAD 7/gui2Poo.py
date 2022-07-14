"""
"""
import tkinter as tk    # importamos librería

class Aplicacion:       # creamos la misma ventana que en gui1 pero usando el paradigma de programación orientada a objetos
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Hola Mundo")
        self.ventana1.mainloop()
        
x = Aplicacion()        
