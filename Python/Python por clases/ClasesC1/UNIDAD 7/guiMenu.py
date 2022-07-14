import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.menu1 = tk.Menu()
        self.ventana1.config(menu = self.menu1)
        opciones1 = tk.Menu(self.menu1)
        opciones1.add_command(label = "Rojo",command=self.Rojo)
        opciones1.add_command(label = "Amarillo",command=self.Amarillo)
        opciones1.add_command(label = "Azul",command=self.Azul)        
        self.menu1.add_cascade(label='Colores',menu=opciones1)
        opciones2 = tk.Menu(self.menu1)
        opciones2.add_cascade(label='640x480',command=self.tamano1)
        opciones2.add_cascade(label='1024x800',command=self.tamano2)
        self.menu1.add_cascade(label='Tamaño', menu=opciones2)
        self.ventana1.mainloop()
        
        
    def Rojo(self):
        self.ventana1.configure(background='red')
    def Amarillo(self):
        self.ventana1.configure(background='yellow')
    def Azul(self):
        self.ventana1.configure(background='blue')
    def tamano1(self):
        self.ventana1.geometry('640x480')
    def tamano2(self):
        self.ventana1.geometry('1024x800')
        
        
x = Aplicacion()