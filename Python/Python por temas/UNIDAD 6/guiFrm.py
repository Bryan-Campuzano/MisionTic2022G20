import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.marco1 = ttk.LabelFrame(self.ventana1, text= 'Login')
        self.marco1.grid(row=0, column=0, padx= 5, pady=10)
        self.login()
        self.ventana1.mainloop()
        
    def login(self):
        self.lblNom = ttk.Label(self.marco1, text ='Usuario:')
        self.lblNom.grid(row=0, column= 0, padx= 4, pady= 4)
        self.entNom = ttk.Entry(self.marco1)
        self.entNom.grid(row=0, column=1)
        
        self.lblPass = ttk.Label(self.marco1, text ='Contraseña:')
        self.lblPass.grid(row=1, column= 0, padx= 4, pady= 4)
        self.entPass = ttk.Entry(self.marco1)
        self.entPass.grid(row=1, column=1)
        
        self.btnAck = ttk.Button(self.marco1, text= 'Ingresar')
        self.btnAck.grid(row=2, column=1, padx= 4, pady= 4)
        
        
        
x = Aplicacion()