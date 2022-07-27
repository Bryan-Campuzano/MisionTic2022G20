""" creamos una aplicación con una lista de ciudades seleccionables para el estudio de las ComboBox y su implementación 
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk    # importamos la librería de tkinter
from tkinter import ttk # importamos la sub-librería ttk
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:   # clase principal de la Aplicacion
    def __init__(self):                                                                                 # metodo constructor de la aplicación
        self.ventana1 = tk.Tk()                                                                         # ventana principal de la interfaz
        self.opcion = tk.StringVar()                                                                    # variable de almacenamiento de cadenas de caracteres que conserva las opciones
        opciones = ("Barranquilla","Cali","Bucaramanga","Medellin")                                     # tupla que almacena las opciones del ComboBox
        self.combo1 = ttk.Combobox(self.ventana1, width=20, textvariable=self.opcion,values= opciones)  # creamos la ComboBox, la posicionamos en la ventana principal, un ancho especifico, una variable de almacenamiento (que cambia dependiendo del estado actual de la Box) y la lista de elementos
        self.combo1.current(0)                                                                          # le damos un valor por defecto, el ComboBox es 
        self.combo1.grid(row=0, column=0)                                                               # ubicamos el elemento en una grilla
        self.lblMostrar = ttk.Label(self.ventana1, text='')                                             # creamos una etiqueta que muestra la opcion actual de la ComboBox
        self.lblMostrar.grid(row=1, column=0)                                                           # ubicamos la etiqueta en la grilla
        self.boton = ttk.Button(self.ventana1, text='Mostar',command=self.mostrar)                      # creamos un boton para desencadenar la acción de 'mostrar'
        self.boton.grid(row=2, column=0)                                                                # ubicamos el boton
        self.ventana1.mainloop()                                                                        # loop principal de la Aplicacion
    def mostrar(self):                                                                                  # creamos el metodo mostrar, este metodo toma el texto actual de la Box y lo muestra en la etiqueta 'mostrar'
        self.lblMostrar['text']= self.opcion.get()

#------------------------INICIALIZACIONES---------------------------
x = Aplicacion()

#   appEnd