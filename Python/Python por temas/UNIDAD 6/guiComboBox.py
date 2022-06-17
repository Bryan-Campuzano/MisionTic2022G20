import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.opcion = tk.StringVar()
        opciones = ("Barranquilla","Cali","Bucaramanga","Medellín")
        self.combo1 = ttk.Combobox(self.ventana1, width=20, textvariable=self.opcion,values= opciones)
        self.combo1.current(0)
        self.combo1.grid(row=0, column=0)
        self.lblMostrar = ttk.Label(self.ventana1, text='')
        self.lblMostrar.grid(row=1, column=0)
        self.boton = ttk.Button(self.ventana1, text='Mostar',command=self.mostrar)
        self.boton.grid(row=2, column=0)
        self.ventana1.mainloop()
    def mostrar(self):
        self.lblMostrar['text']= self.opcion.get()

x = Aplicacion()