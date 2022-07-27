""" construimos una aplicación que permite simular un 'login' de usuario para el estudio de entradas y frames 
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk    # importamos la librería de tkinter
from tkinter import ttk # importamos la sub-librería de ttk
#------------------------ZONA DE CÓDIGO------------------------
class Aplicacion:                                                       # clase principal de la aplicación
    def __init__(self):                                                 # método constructor de la aplicación
        self.ventana1 = tk.Tk()                                         # creamos la ventana principal                
        self.marco1 = ttk.LabelFrame(self.ventana1, text= 'Login')      # creamos un frame, es un contenedor gráfico similar a grip pero permite manejarlo como un elemento gráfico, sin necesidad de editar los parámetros propios de la ventana
        self.marco1.grid(row=0, column=0, padx= 5, pady=10)             # lo ubicamos en una grilla pero con dos parámetros extras, 'padx' y 'pady' que son las margenes entre el elemento principal y los elementos internos
        self.login()                                                    # ejecutamos el método login, que modelaremos después, esto se hace para poder 'compartimentalizar' y tener un codigo mas modular
        self.ventana1.mainloop()                                        # loop principal de la aplicación
        
    def login(self):                                                    # método que modela el login
        self.lblNom = ttk.Label(self.marco1, text ='Usuario:')          # creamos una etiqueta con el texto 'Usuario' y lo ubicamos en el marco 1
        self.lblNom.grid(row=0, column= 0, padx= 4, pady= 4)            # ubicamos la etiqueta en el marco modificando el parámetro grid
        self.entNom = ttk.Entry(self.marco1)                            # creamos una entrada de texto 
        self.entNom.grid(row=0, column=1)                               # ubicamos esta entrada al frente de la etiqueta 'Usuario'
        
        self.lblPass = ttk.Label(self.marco1, text ='Contraseña:')      # creamos otra etiqueta y otra entrada para modelar el dato 'Contraseña' como segundo item del login
        self.lblPass.grid(row=1, column= 0, padx= 4, pady= 4)
        self.entPass = ttk.Entry(self.marco1)
        self.entPass.grid(row=1, column=1)
        
        self.btnAck = ttk.Button(self.marco1, text= 'Ingresar')         # creamos un boton de ingreso para simular el envió de un formulario
        self.btnAck.grid(row=2, column=1, padx= 4, pady= 4)
        
        
#------------------------INICIALIZACIONES---------------------------      
x = Aplicacion()

#   appEnd