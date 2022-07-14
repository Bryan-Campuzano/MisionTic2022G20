# REalizar una aplicación que tenga dos botones para incrementar o
# decrementare un contador, que se muestra en una etiqueta(Label)

import tkinter as tk

class Aplicacion():
    def __init__(self):
        self.contador = 0
        self.ventana1 = tk.Tk()
        self.ventana1.title('Contador')
        self.lblConta= tk.Label(self.ventana1, text=self.contador, foreground='red')
        self.lblConta.grid(row=0,column=1)
        self.btnInc = tk.Button(self.ventana1, text= 'Incrementar', command=self.incrementar)
        self.btnInc.grid(row=1,column=0)
        self.btnDec = tk.Button(self.ventana1,text= 'Decrementar', command=self.decrementar)
        self.btnDec.grid(row=1,column=2)
        self.ventana1.mainloop()
    
    def incrementar(self):
        self.contador +=1
        self.lblConta['text'] = self.contador
        
    def decrementar(self):
        self.contador -=1
        self.lblConta['text'] = self.contador
        
x = Aplicacion()
        