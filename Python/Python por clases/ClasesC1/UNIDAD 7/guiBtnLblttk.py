""" Realizar una aplicación que tenga dos botones para incrementar o disminuir un contador, que se muestra en una etiqueta(Label)
    em esta ocasión para el estudio de elementos pertenecientes a la sub-librería ttk, la cual contiene elementos de carácter visual
    mas moderno
"""
#------------------------IMPORTACIONES---------------------------
import tkinter as tk        # importamos la librería de tkinter
from tkinter import ttk     # importamos ttk
#------------------------ZONA DE CÓDIGO------------------------

# básicamente en esta sub-librería podemos manejar los mismos elementos gráficos que 'tk' pero con apariencia diferente
# la construcción de esta aplicación es la misma que en 'GuiBtnLbl' pero con apariencia diferente
class Aplicacion():
    def __init__(self):                                                                         # metodo constructor de la Aplicacion
        self.contador = 0                                                                       # inicializamos una variable que almacena el valor de un contador
        self.ventana1 = tk.Tk()                                                                 # creamos la ventana principal
        self.ventana1.title('Contador')                                                         # designamos 'Contador' como el titulo de la ventana
        self.lblConta= ttk.Label(self.ventana1, text=self.contador, foreground='red')           
        self.lblConta.grid(row=0,column=1)
        self.btnInc = ttk.Button(self.ventana1, text= 'Incrementar', command=self.incrementar)
        self.btnInc.grid(row=1,column=0)
        self.btnDec = ttk.Button(self.ventana1,text= 'Disminuir', command=self.disminuir)
        self.btnDec.grid(row=1,column=2)
        self.ventana1.mainloop()
    
    def incrementar(self):
        self.contador +=1
        self.lblConta['text'] = self.contador
        
    def disminuir(self):
        self.contador -=1
        self.lblConta['text'] = self.contador
        
#------------------------INICIALIZACIONES--------------------------- 
x = Aplicacion()

#   appEnd
        