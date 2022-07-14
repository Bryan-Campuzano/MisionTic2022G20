""" Realizar una aplicación que tenga dos botones para incrementar o disminuir un contador, que se muestra en una etiqueta(Label)
    usaremos un par de widgets para la realización de esta Aplicacion, las 'labels' o etiquetas, que permiten la representación de texto
    en la interfaz y los 'button' o botón, ejecutan una acción especifica cuando se hace click sobre ellos
"""
import tkinter as tk    # importamos librería

class Aplicacion():     # iniciamos la Aplicacion, incluyendo los elementos gráficos
    def __init__(self):
        self.contador = 0                                                                       # inicializamos un contador
        self.ventana1 = tk.Tk()                                                                 # ventana principal
        self.ventana1.title('Contador')                                                         # nombre de la ventana principal
        self.lblConta= tk.Label(self.ventana1, text=self.contador, foreground='red')            # 'lbl' siglas de 'label' inicializamos la etiqueta con parámetros de inicio 
                                                                                                # como a que ventana pertenece, el texto que lleva y color del texto
        self.lblConta.grid(row=0,column=1)                                                      # el método grid crea una rejilla y permite localizar el elemento a una posición especifica
        self.btnInc = tk.Button(self.ventana1, text= 'Incrementar', command=self.incrementar)   # creamos un botón, recibe como parámetro, la ventana a la que pertenece, el texto interior y la acción a realizar cuando se hace click
        self.btnInc.grid(row=1,column=0)                                                        # le asignamos un lugar especifico al botón
        self.btnDec = tk.Button(self.ventana1,text= 'Disminuir', command=self.disminuir)        # creamos el botón encargado de disminuir el contador
        self.btnDec.grid(row=1,column=2)                                                        # lo ubicamos en la grilla 
        self.ventana1.mainloop()                                                                # loop principal de la ventana
    
    def incrementar(self):  # incrementa el valor del contador cuando es ejecutado
        self.contador +=1
        self.lblConta['text'] = self.contador
        
    def disminuir(self):    # disminuye el valor del contador cuando es ejecutado
        self.contador -=1
        self.lblConta['text'] = self.contador
        
x = Aplicacion()    # creamos un elemento de tipo 'Aplicacion' para ejecutar la ventana
        